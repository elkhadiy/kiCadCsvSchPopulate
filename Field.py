class Field:
    'Class representing a field entry in a component description'
    def __init__(self, field_number, value, orientation, posX, posY, size, Flags, moduleType, unknown, name):
        self.field_number = field_number
        self.value = value
        self.orientation = orientation
        self.posX = posX
        self.posY = posY
        self.size = size
        self.Flags = Flags
        self.moduleType = moduleType
        self.unknown = unknown
        self.name = name

    def __str__(self):
        return "".join((
                    "F ", self.field_number, " ", self.value, " ", self.orientation, " ",
                    self.posX, " ", self.posY, " ", self.size, " ", self.Flags, " ", self.moduleType, " ", self.unknown, " ", self.name, "\n"
                    ))

if __name__ == "__main__":
    f = Field("0","uC1","H","120","240","60","0000","L","CNN","something")
    print f
