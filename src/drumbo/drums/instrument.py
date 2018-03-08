class Instrument:

    sample = None
    name = None

    def __init__(self, pattern_str):
        self.pattern = pattern_str
        self.steps = self.pattern.split('|')[1:-1]