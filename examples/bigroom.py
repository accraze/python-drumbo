from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat

song = Song('Big Room Beat', bpm=126, steps=16)

kik_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'
snr_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'
hat_str = '|_|_|_|X|_|_|X|_|_|_|_|X|_|_|X|_|'

kick = Kick(kik_str, attack=30, decay=40)
snare = Snare(snr_str)
hihat = HiHat(hat_str)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('Thanks for groovin!')
