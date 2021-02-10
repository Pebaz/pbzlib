from pbz.cli.command import Command, ArgList


class hello(Command):
    """
    Says "Hello World!"

    $ pbz hello
    """
    def execute(self, args: ArgList) -> None:
        self.say_hello()
    
    def say_hello(self):
        print('Hello World!')
