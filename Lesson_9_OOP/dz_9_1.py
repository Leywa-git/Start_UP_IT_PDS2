class Automobile:
    def __init__(self, model, colour, engine_volume):
        self.model = model
        self.colour = colour
        self.engine_volume = engine_volume

    def drive_forward(self):
        print("Vehicle", self.colour, self.model, self.engine_volume, "is driving forward")

    def drive_backwards(self):
        print("Vehicle", self.colour, self.model, self.engine_volume, "is driving backwards")


class AutomobileExtended(Automobile):
    def turn_right(self):
        print("Vehicle", self.colour, self.model, self.engine_volume, "is turning right")

    def turn_left(self):
        print("Vehicle", self.colour, self.model, self.engine_volume, "is turning left")


auto_navigation = AutomobileExtended("Dodge Charger", "black", 5.7)
auto_navigation.drive_forward()
auto_navigation.drive_backwards()
auto_navigation.turn_right()
auto_navigation.turn_left()
