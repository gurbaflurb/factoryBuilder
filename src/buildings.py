
class Building:
    def __init__(self, inputs, outputs, power):
        self.inputs = inputs
        self.outputs = outputs
        self.power = power
    
    def get_inputs(self):
        return self.inputs

    def get_outputs(self):
        return self.outputs
        
    def get_power(self):
        return self.power
