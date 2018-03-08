import sys
import unittest

from drumbo.drums import HiHat
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.song import Song


class TestSong(unittest.TestCase):

    def test_init(self):
        title = 'test'
        s = Song(title)
        self.assertEquals(s.bpm, 120)
        self.assertEquals(s.title, title)

    def test_add(self):
        s = Song('test2')
        self.assertEquals(s.drums, [])
        k = Kick('|X|_|_|_|X|_|_|_|')
        s.add(k)
        self.assertEquals(len(s.drums), 1)

    def test_play(self):
        song = Song('breaks')
        kick = Kick('|X|_|_|_|X|_|_|_|')
        snare = Snare('|_|_|_|_|X|_|_|_|')
        hihat = HiHat('|_|_|X|_|_|_|X|_|')
        song.add(kick)
        song.add(snare)
        song.add(hihat)

        class MockOutput(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)
        stdout_org = sys.stdout
        mock_stdout = MockOutput()
        try:
            sys.stdout = mock_stdout
            song.play()
        finally:
            sys.stdout = stdout_org
        pattern = '|Kick|_|HiHat|_|Kick+Snare|_|HiHat|_|\n'
        self.assertEquals(str(mock_stdout), pattern)
