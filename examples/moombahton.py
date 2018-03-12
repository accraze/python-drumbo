from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat


song = Song('Moombahton', bpm=108, steps=32)

kik_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'
snr_str = '|_|_|_|X|_|_|X|_|_|_|_|X|_|_|X|_|_|_|_|X|_|_|X|_|_|_|_|X|_|_|X|_|'
hat_str = '|_|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|'

kick = Kick(kik_str, attack=43, decay=31)
snare = Snare(snr_str, decay=11)
hihat = HiHat(hat_str, decay=27)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('Thanks for groovin!')
