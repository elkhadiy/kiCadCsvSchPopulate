#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys, os, csv

def groupby(key, csvFile):
    reader = csv.reader(open(csvFile), delimiter=',')
    result = {}
    attrs = reader.next()

    for row in reader:
        rkey = (row[attrs.index(key[0])], row[attrs.index(key[1])])
        if rkey[0] != '' and rkey[1] != '':
            if rkey in result:
                result[rkey] += 1
            else:
                result[rkey] = 1

    return result

if __name__ == "__main__":
    res = groupby(("Fabricant","Référence"),sys.argv[1])
    print "Fabricant, Référence, Nombre"
    for k in res:
        print k[0],", ", k[1], ", ", res[k]