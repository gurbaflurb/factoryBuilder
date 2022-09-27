from buildings import Building

class IronMine(Building):
    def __init__(self, inputs, outputs, power, iron_per_min):
        self.inputs = inputs
        self.outputs = outputs
        self.power = power
        self.iron_per_min = iron_per_min
    
    def get_iron_per_min(self):
        return self.iron_per_min
