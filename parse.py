#!/usr/bin/python

from optparse import OptionParser
import sys, os, csv
from SchFile import SchFile

def loadCSVResources(csvFile):
    reader = csv.reader(open(csvFile), delimiter=';')
    result = {}
    attrs = reader.next()
    dupkeys = []
    for row in reader:
        key = (row[0], row[1])
        if key in result:
            if key != ('',''):
                dupkeys.append(key)
            pass
        result[key] = row[:]
    print "Found ", len(dupkeys), " duplicate keys in csv file :"
    for k in dupkeys:
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
    outfile = open("DEBUG_outputfile.sch", "w")
    outfile.write(str(infile))
    outfile.close()


if __name__ == "__main__":
    parseFiles()
