from tires.tires import Tires

class Carrigan(Tires):
    def __init__(self,wear):
        self.wear = wear

    def needs_change(self):
        for i in range(4):
            if self.wear[i] >= 0.9:
                return True
        return False