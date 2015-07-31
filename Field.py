class Field:
    'Class representing a field entry in a component description'
    def __init__(self, field_number, value, orientation, posX, posY, size, Flags, name):
        self.field_number = field_number
        self.value = value
        self.orientation = orientation
        self.posX = posX
        self.posY = posY
        self.size = size
        self.Flags = Flags
        self.name = name

    def __str__(self):
        return "".join((
                    "F ", self.field_number, " ", self.value, " ", self.orientation, " ",
                    self.posX, " ", self.posY, " ", self.size, " ", self.Flags, " ", self.name, "\n"
                    ))
