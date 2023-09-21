from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self,wear):
        self.wear = wear

    def needs_change(self):
        sum = 0
        for i in range(4):
            sum += self.wear[i]
        if sum >= 3:
            return True
        else:
            return False
