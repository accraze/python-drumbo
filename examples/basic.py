from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat

# default 8 step sequence at 120 BPM

song = Song('basic')

kick   = Kick('|X|_|_|_|X|_|_|_|')
snare = Snare('|_|_|_|_|X|_|_|_|')
hihat = HiHat('|_|_|X|_|_|_|X|_|')

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('Ok, done for now :)')
