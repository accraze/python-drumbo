from drumbo.song import Song
from drumbo.drums import Kick
from drumbo.drums import Snare
from drumbo.drums import HiHat


song = Song('Trap Beat', bpm=147, steps=32)

kik_str = '|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'

kick = Kick(kik_str, attack=40, decay=63)
snare = Snare(snr_str, decay=40)
hihat = HiHat(hat_str, decay=30)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()
song.reset()

kik_str = '|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'

kick = Kick(kik_str, attack=40, decay=63)
snare = Snare(snr_str, decay=40)
hihat = HiHat(hat_str, decay=30)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()
song.reset()

kik_str = '|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'

kick = Kick(kik_str, attack=40, decay=63)
snare = Snare(snr_str, decay=40)
hihat = HiHat(hat_str, decay=30)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()
song.reset()

kik_str = '|X|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
snr_str = '|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|X|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|'
hat_str = '|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|X|_|_|_|'

kick = Kick(kik_str, attack=40, decay=63)
snare = Snare(snr_str, decay=40)
hihat = HiHat(hat_str, decay=30)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()
song.reset()

print('YEEEEAAAAAAH')
