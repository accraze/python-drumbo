from drumbo.drums import Kick, Snare, HiHat
from drumbo.song import Song


song = Song('Hardcore Junglist Massive', bpm=160, steps=32)

kik_str = '|X|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|X|_|X|_|_|_|_|_|_|_|X|_|_|_|_|_|'
snr_str = '|_|_|_|_|X|_|X|_|_|X|_|_|X|_|_|X|_|_|_|_|X|_|X|_|_|X|_|_|X|_|_|X|'
hat_str = '|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|X|_|'

kick = Kick(kik_str, attack=26, decay=4)  # short fast beat
snare = Snare(snr_str, attack=26, decay=40)
hihat = HiHat(hat_str, decay=28)

song.add(kick)
song.add(snare)
song.add(hihat)

song.play()

print('Wicked, Wicked, Junglist massive!')
