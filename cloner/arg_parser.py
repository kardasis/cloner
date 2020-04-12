class ArgParser:
    def __init__(self, args):
        if len(args) == 0:
            raise ValueError('Must provide at least one argument')
        if len(args) > 2:
            raise ValueError('Too many arguments')
        self.set_url(args)

    def set_url(self, args):
        pass

