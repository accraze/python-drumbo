from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat


song = Song('Wubwubuwubwub', bpm=140, steps=32)

kik_str = '|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|_|_|_|X|_|X|_|X|_|_|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|_|_|'

kick = Kick(kik_str, attack=43, decay=31)
snare = Snare(snr_str, decay=11)
hihat = HiHat(hat_str, decay=27)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()
song.reset()

kik_str = '|X|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|X|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|_|_|_|X|_|X|_|_|_|X|_|X|_|X|_|X|_|_|_|X|_|_|_|X|_|X|_|X|_|X|_|'

kick = Kick(kik_str, attack=43, decay=31)
snare = Snare(snr_str, decay=11)
hihat = HiHat(hat_str, decay=27)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('( ( ( Wubwubuwubwub wuububbbb ) ) )')
