from urllib.parse import urlparse
import posixpath


class ArgParser:
    def __init__(self, args):
        if len(args) == 0:
            raise ValueError('Must provide at least one argument')
        if len(args) > 2:
            raise ValueError('Too many arguments')
        self.set_url(args)

    def set_url(self, args):
        if len(args) == 2:
            self.url = f'git@github.com:{args[0]}/{args[1]}.git'

        if len(args) == 1:
            http_url = args[0]
            path = urlparse(http_url).path
            path = posixpath.split(path)
            user_name = path[0][1:]
            self.url = f'git@github.com:{user_name}/{repo_name}.git'
