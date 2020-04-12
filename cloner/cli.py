import click
import os

from cloner.arg_parser import ArgParser


class ClonerException(click.ClickException):
    exit_code = 1


@click.command()
@click.argument('args', nargs=-1)
def main(args):
    cloner_path = os.getenv('CLONER_PATH')
    if cloner_path is None:
        msg = 'CLONER_PATH environment variable must be defined'
        raise click.ClonerException(msg)
    ArgParser(args)


if __name__ == '__main__':
    main()
