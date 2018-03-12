"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m drumbo` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``drumbo.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``drumbo.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
from subprocess import call

prompt_str = 'Which song do you want to play?\n \
 - Basic\n \
 - BigRoom\n \
 - Dubstep\n \
 - House\n \
 - Jungle\n \
 - Moombahton\n \
 - Techstep\n \
 - Trapbeat\n'

choices = ['Basic', 'BigRoom', 'Dubstep', 'House',
           'Jungle', 'Moombahton', 'Techstep', 'Trapbeat']


@click.command()
@click.option('--title', prompt=prompt_str, type=click.Choice(choices))
def main(title):
    click.echo('Playing song: {}'.format(title))
    fname = 'examples/{}.py'.format(title.lower())
    call(['python3', fname])

# @click.argument('names', nargs=-1)
# def main(names):
#     click.echo(repr(names))
