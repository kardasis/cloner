from urllib.parse import urlparse
import posixpath


class ArgParser:
    def __init__(self, args):
        if len(args) == 0:
            raise ValueError('Must provide at least one argument')
        if len(args) > 2:
            raise ValueError('Too many arguments')
        self.parse_args(args)

    def parse_args(self, args):
        if len(args) == 2:
            self.url = f'git@github.com:{args[0]}/{args[1]}.git'

        if len(args) == 1:
            http_url = args[0]
            path = urlparse(http_url).path
            path_components = []
            while path != '/':
                path, tail = posixpath.split(path)
                path_components.append(tail)
            self.user_name = path_components[-1]
            self.repo_name = path_components[-2]
