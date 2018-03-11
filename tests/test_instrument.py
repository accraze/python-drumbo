import unittest

from drumbo.drums import Instrument


class TestInstrument(unittest.TestCase):

    def test_init(self):
        pattern = '|X|_|_|_|X|_|_|_|'
        i = Instrument(pattern)
        self.assertEquals(i.name, None)
        self.assertEquals(i.sample, None)
        self.assertEquals(i.attack, 50)
        self.assertEquals(i.decay, 50)

        i2 = Instrument(pattern, attack=23, decay=40)
        self.assertEquals(i2.attack, 23)
        self.assertEquals(i2.decay, 40)
