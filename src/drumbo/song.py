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
        Raise error if pattern length
        does not match global steps count.
        """
        if not self._matching_steps(drum.steps):
            raise Exception('Incorrect pattern step amount')
        self.drums.append(drum)

    def play(self):
        """
        Plays all the song's
        patterns in real-time:
        |Kick|_|HiHat|_|Kick+Snare|_|...
        """
        self._print('|', delay=False)
        for step in range(self.steps):
            note = self._get_step_output(step)
            self._print(note + '|')
            # line break for every bar
            self._check_newline(step)

    def _print(self, msg, delay=True):
        """
        Prints a step's note(s) to
        stdout for tempo-timed output.
        """
        sys.stdout.write(msg)
        sys.stdout.flush()
        if delay:
            import time
            time.sleep(self._timing_delay)

    @property
    def _timing_delay(self):
        """
        Calculates how many
        seconds for each step.
        """
        return (60/self.bpm) * .5

    def _matching_steps(self, pattern):
        """
        Checks if a given pattern
        matches the song's global
        step count.
        """
        if len(pattern) != self.steps:
            return False
        return True

    def _get_step_output(self, step):
        """
        Returns notes played
        for each step as string
        otherwise, return '_'
        """
        output = self._render_output(step)
        if not output:
            output = '_'
        return output

    def _render_output(self, step):
        """
        Combines all instrument names
        for a given step.
        """
        output = ''
        multi = False
        for drum in self.drums:
            if drum.steps[step] != '_':
                if multi:
                    # more than one instrument played
                    # on current step, so concatenate
                    output += '+{}'.format(drum.name)
                else:
                    output += drum.name
                    multi = True
        return output

    def _check_newline(self, step):
        """
        Prints line break
        for each bar (8 steps)
        """
        if step % 7 == 0 and step != 0:
            self._print('\n', delay=False)
            if (step + 1) < self.steps:
                self._print('|', delay=False)
