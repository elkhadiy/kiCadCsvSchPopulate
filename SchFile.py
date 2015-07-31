import Component, Field

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
        while line != "$Comp":
            headerContent.append(line)
            line = lineiter.next()
        self.header = "".join(headerContent)

        # Parsing components
        self.components = []
        line = lineiter.next()
        while line != "$EndSCHEMATC":
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
                            sline[5], sline[6], sline[7], sline[8], "" if len(sline)==9 else sline[9]))
                line = lineiter.next()
            # useless line
            line = lineiter.next()
            A = line.split()[0]
            B = line.split()[1]
            C = line.split()[2]
            D = line.split()[3]
            line = lineiter.next() # $EndComp
            self.components.append(
                        Component(L[0], L[1], U[0], U[1], U[2], P[0], P[1], F, A, B, C, D)
                            )
            while line != "$Comp" or line != "$EndSCHEMATC":
                line = lineiter.next()

    def __str__(self):
        ret = [self.header]
        ret.extend(self.components)
        ret.append("$EndSCHEMATC")
