from Component import Component
from Field import Field

class SchFile:
    'Class representing an sch file'
    def __init__(self, filename):
        fil = open(filename, "r")
        fileContent = fil.readlines()
        fil.close()
        lineiter = iter(fileContent)

        # Construct header
        line = lineiter.next()
        headerContent = [line]
        while line != "$Comp\n":
            headerContent.append(line)
            line = lineiter.next()
        self.header = "".join(headerContent)

        self.filelist = [self.header]

        # Parsing components
        self.components = []
        while line != "$EndSCHEMATC\n":
            line = lineiter.next()
            L = line.split()
            line = lineiter.next()
            U = line.split()
            line = lineiter.next()
            P = line.split()
            F = []
            line = lineiter.next()
            while line[0] == "F":
                sline = line.split()
                F.append(Field(sline[1], sline[2], sline[3], sline[4],
                            sline[5], sline[6], sline[7], sline[8], sline[9], "" if len(sline)==10 else sline[10]))
                line = lineiter.next()
            # useless line
            line = lineiter.next()
            A = line.split()[0]
            B = line.split()[1]
            C = line.split()[2]
            D = line.split()[3]
            line = lineiter.next() # $EndComp
            c = Component(L[1], L[2], U[1], U[2], U[3], P[1], P[2], F, A, B, C, D)
            self.components.append(c)
            self.filelist.append(c)
            between2comp = []
            while line != "$Comp\n" and line != "$EndSCHEMATC\n":
                line = lineiter.next()
                if line != "$Comp\n":
                    between2comp.append(line)
            self.filelist.extend(between2comp)

    def __str__(self):
        ret = []
        for l in self.filelist:
            ret.append(str(l))
        return "".join(ret)
