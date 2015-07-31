import Field

class Component:
    'Class containing component documentation and information'
    def __init__(self, name, reference, N, mm, time_stamp, posX, posY, fields, A, B, C, D):
        self.name = name
        self.reference = reference
        self.N = N
        self.mm = mm
        self.time_stamp = time_stamp
        self.posX = posX
        self.posY = posY
        self.fields = fields
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def __str__(self):
        ret = [ "$Comp\n"
                "L ", self.name, " ", self.reference, "\n",
                "U ", self.N, " ", self.mm, " ", self.time_stamp, "\n",
                "P ", self.posX, " ", self.posY, "\n"
                ]
        ret.extend(self.fields)
        ret.extend([
                    "1 ", self.posX, " ", self.posY, "\n",
                    self.A, " ", self.B, " ", self.C, " ", self.D, "\n",
                    "$EndComp\n"
                ])
        return "".join(ret)


