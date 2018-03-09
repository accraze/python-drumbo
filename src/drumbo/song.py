import sys


class Song:

    def __init__(self, title, bpm=120, steps=8):
        self.title = title
        self.bpm = bpm
        self.steps = steps
        self.drums = []

    def add(self, drum):
        """
        Adds a drum pattern to the song.
        If the pattern's length does not match
        the song's step count, we throw
        an error.
        """
        if not self._matching_steps(drum.steps):
            raise Exception('Incorrect pattern step amount')
        self.drums.append(drum)

    def play(self):
        self._print('|')
        for step in range(self.steps):
            note = '{}'.format(self._step_output(step))
            self._print(note + '|')
            if (step + 1) % self.steps == 0:
                self._print('\n', delay=False)

    def _print(self, letter, delay=True):
        sys.stdout.write(letter)
        sys.stdout.flush()
        if delay:
            import time
            time.sleep(self._timing_delay)

    @property
    def _timing_delay(self):
        return (60/self.bpm) * .5

    def _matching_steps(self, pattern):
        if len(pattern) != self.steps:
            return False
        return True

    def _step_output(self, step):
        output = ''
        multi = False
        for drum in self.drums:
            if drum.steps[step] != '_':
                if multi:
                    output += '+{}'.format(drum.name)
                else:
                    output += drum.name
                    multi = True
        if not output:
            output = '_'
        return output
