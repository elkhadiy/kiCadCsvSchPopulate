from Field import Field

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
        for f in self.fields:
            ret.append(str(f))
        ret.extend([
                    "1 ", self.posX, " ", self.posY, "\n",
                    self.A, " ", self.B, " ", self.C, " ", self.D, "\n",
                    "$EndComp\n"
                ])
        return "".join(ret)

if __name__ == "__main__":
    f0 = Field("0","\"#PWR054\"","H","9150","610","30","0001","C","CNN","")
    f1 = Field("1","+3.3V","H","9150","760","30","0000","C","CNN","")
    f2 = Field("2","\"\"","H","9150","760","60","0000","C","CNN","")
    f3 = Field("3","\"\"","H","9150","760","60","0000","C","CNN","")
    c0 = Component("+3.3V", "#PWR054", "1", "1", "55AC015D", "9150", "650", [f0, f1, f2, f3], "-1", "0", "0", "1")
    print c0
