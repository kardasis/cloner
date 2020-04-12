import click
import os


class Cli:
    def __init__(self, args):
        if len(args) == 0:
            raise ClonerException('Must provide at least one argument')
        if len(args) > 2:
            raise ClonerException('Too many arguments')


class ClonerException(click.ClickException):
    exit_code = 1


@click.command()
@click.argument('args', nargs=-1)
def main(args):
    cloner_path = os.getenv('CLONER_PATH')
    if cloner_path is None:
        msg = 'CLONER_PATH environment variable must be defined'
        raise click.ClonerException(msg)
    cli = Cli(args)


if __name__ == '__main__':
    main()
