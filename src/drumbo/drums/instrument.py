class Instrument:

    sample = None
    name = None

    def __init__(self, pattern_str, attack=50, decay=50):
        self.pattern = pattern_str
        self.steps = self.pattern.split('|')[1:-1]
        self.attack = attack
        self.decay = decay
