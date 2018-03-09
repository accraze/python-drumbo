=====
Usage
=====

To use drumbo in a project::

	import drumbo
    
Here is an example on how you might sequence a song::

    from drumbo.song import Song
    from drumbo.drums.kick import Kick
    from drumbo.drums.snare import Snare
    from drumbo.drums.hihat import HiHat

    song = Song('breaks')

    kick   = Kick('|X|_|_|_|X|_|_|_|')
    snare = Snare('|_|_|_|_|X|_|_|_|')
    hihat = HiHat('|_|_|X|_|_|_|X|_|')

    song.add(kick)
    song.add(snare)
    song.add(hihat)

    song.play()
