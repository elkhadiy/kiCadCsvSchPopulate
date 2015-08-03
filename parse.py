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
    dupkeys = []
    nofingerprint = []
    for row in reader:
        key = (row[5], row[1])
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
    return result

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

    resourceDict = loadCSVResources(options.inputfile)
    infile = SchFile(options.outputfile)

    dic = {}
    for comp in infile.components:
        if comp.fields[2].value != "" and comp.fields[2].value != "~" and comp.fields[2].value != "NPTH":
            dic[(comp.fields[2].value, comp.fields[1].value)] = comp

    FIELD_TEXT_SIZE = "60"

    print "Composant(s) à modifier : "
    for key, value in dic.iteritems():
        #print key, " :: ", resourceDict[key]
        dic[key].fields[2].Flags = "0001"
        # Get documentation
        dic[key].fields[3].value = resourceDict[key][13]
        dic[key].fields[3].Flags = "0001"
        # Get manufacturer
        dic[key].fields[4] = Field("4", resourceDict[key][6], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Manufacturer")
        #Get reference
        dic[key].fields[5] = Field("5", resourceDict[key][7], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Reference")
        #Get Digikey reference
        dic[key].fields[6] = Field("6", resourceDict[key][8], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Digikey Reference")
        #Get Digikey USA link
        dic[key].fields[7] = Field("7", resourceDict[key][9], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Digikey USA Link")
        #Get Digikey FR link
        dic[key].fields[8] = Field("8", resourceDict[key][10], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Digikey FR Link")
        #Get Farnell link
        dic[key].fields[9] = Field("9", resourceDict[key][11], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Farnell link")
        #Get Octopart Link
        dic[key].fields[10] = Field("10", resourceDict[key][12], "H", dic[key].posX, dic[key].posY, FIELD_TEXT_SIZE,
                                    "0001", "C", "CNN", "Octopart link")

    outfile = open("DEBUG_outputfile.sch", "w")
    outfile.write(str(infile))
    outfile.close()


if __name__ == "__main__":
    parseFiles()
