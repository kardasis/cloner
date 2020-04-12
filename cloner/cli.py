import click
import os


@click.command()
def main(git_user, git_repo):
    cloner_path = os.getenv('CLONER_PATH')
    if cloner_path is None:
        msg = 'CLONER_PATH environment variable must be defined'
        exc = click.ClickException(msg)
        exc.exit_code = 1
        raise exc
