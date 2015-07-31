#!/usr/bin/python

from optparse import OptionParser
import sys, os, copy, SchFile

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

    infile = open(options.inputfile, "r", 1)
    outfile = open(options.outputfile, "r")

    print 'kiCad File to populate : ', outfile.name

    outfileContent = outfile.readlines()
    outfile.close()
    for line in outfileContent:
        index = line.find('hey')
        if index != -1:
            print 'index : ', index, 'line : ', line
            print outfileContent
            print str(outfileContent.index(line))
            outfileContent.insert(outfileContent.index(line)+1,'I found what I was looking for!\n')
            break

    outfile = open(outfile.name, "w")
    outfileContent = "".join(outfileContent)
    outfile.write(outfileContent)
    outfile.close()


if __name__ == "__main__":
    parseFiles()
