from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat


song = Song('Classic House', bpm=120, steps=32)

kik_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|X|_|'
snr_str = '|_|_|_|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|X|_|_|_|'
hat_str = '|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|X|X|_|'

kick = Kick(kik_str, attack=17, decay=15)
snare = Snare(snr_str, attack=22, decay=12)
hihat = HiHat(hat_str, decay=18)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('Hope you enjoyed house music :)')
