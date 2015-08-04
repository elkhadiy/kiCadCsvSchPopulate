#!/usr/bin/python
# vim: set fileencoding=utf-8 :

from optparse import OptionParser
import sys, os, csv
from SchFile import SchFile
from Field import Field

def loadCSVResources(csvFile):
    reader = csv.reader(open(csvFile), delimiter=',')
    result = {}
    attrs = reader.next()
    nonStandardFields = attrs[attrs.index("Empreinte")+1:attrs.index("Datasheet")]
    dupkeys = []
    nofingerprint = []
    for row in reader:
        key = (row[attrs.index("Empreinte")], row[attrs.index("Valeur")])
        if key[0] == '':
            if key != ('', ''):
                nofingerprint.append(row)
        elif key in result:
            if key != ('',''):
                dupkeys.append(row)
        else:
            result[key] = row[:]
    print "Found ", len(dupkeys), " duplicate keys in csv file :"
    for k in dupkeys:
        print k
    print "Found ", len(nofingerprint), " components with no fingerprint in csv file :"
    for k in nofingerprint:
        print k
    return result, nonStandardFields

def parseFiles():
    usage = "usage: %prog [-i | --ifile] <inputfile> [-o | --ofile] <outputfile>"
    version = "%prog 1.0"
    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-i", "--ifile",
                    action="store", type="string", dest="inputfile",
                    help="Input file containing component info")
    parser.add_option("-o", "--ofile",
                    action="store", type="string", dest="outputfile",
                    help="Output file where to populate component info (kiCad for example)")

    (options, args) = parser.parse_args()

    if options.inputfile == None:
        parser.error("Must supply an input file!")
        sys.exit(2)

    if options.outputfile == None:
        parser.error("Must supply an output file!")
        sys.exit(2)
    
    if not (os.path.isfile(options.inputfile) and os.path.isfile(options.outputfile)):
        parser.error("Files supplied in the command line do not exist");
        sys.exit(2);

    resourceDict, nonStandardFields = loadCSVResources(options.inputfile)
    infile = SchFile(options.outputfile)

    # Dictionary containing components from the sch file
    dic = {}
    for comp in infile.components:
        # The dictionnary values are lists
        try:
            dic[(comp.fields[2].value, comp.fields[1].value)].append(comp)
        except KeyError:
            dic[(comp.fields[2].value, comp.fields[1].value)] = [comp]

    FIELD_TEXT_SIZE = "60"

    # for each component present in sch try to find info about it in the database
    componentNotInDatabase = []
    for key, value in dic.iteritems():
        for comp in dic[key]:
            try:
                # Hide the value field (always at 2 in database)
                comp.fields[2].Flags = "0001"
                # Add documentation (always at 3 in database)
                comp.fields[3].value = resourceDict[key][5+len(nonStandardFields)+1]
                comp.fields[3].Flags = "0001"

                i = 0
                FIELD_OFFSET_IN_SCH = 4
                FIELD_OFFSET_IN_CSV = 6
                for field in nonStandardFields:
                    comp.fields[i+FIELD_OFFSET_IN_SCH] = Field(str(i+FIELD_OFFSET_IN_SCH),
                                        resourceDict[key][i+FIELD_OFFSET_IN_CSV], "H",
                                        comp.posX, comp.posY, FIELD_TEXT_SIZE,
                                        "0001", "C", "CNN", nonStandardFields[i])
                    i += 1
            except:
                componentNotInDatabase.append(comp)

    print "found ", len(componentNotInDatabase), " components present in sch and not in csv : (thus not updated)"
    for comp in componentNotInDatabase:
        print comp


    outfile = open("DEBUG_outputfile.sch", "w")
    outfile.write(str(infile))
    outfile.close()


if __name__ == "__main__":
    parseFiles()
