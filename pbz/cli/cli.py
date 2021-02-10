import importlib
from typing import List


# TODO(pebaz): Use command packages, not command modules
class CLI:
    def __init__(self):
        self.commands = {
            command.__name__: command()
            for command in self.get_commands()
        }

    def get_commands(self) -> List[Command]:
        command_modules = [
            importlib.import_module(f'pbz.cli.commands.{cmd.stem}')
            for cmd in (Path(__file__).parent / 'commands').iterdir()
            if cmd.name.startswith('cmd_')  # Ignore helper modules
        ]

        commands = []
        for cmd in commnad_modules:
            commands.extend([
                name for name in filter(
                    lambda x: x is not Command,
                    cmd.__dict__.values()
                )
                if isinstance(name, type) and issubclass(name, Command)
            ])
    
    def main(self, args: List[str]) -> None:
        if len(args) < 1:
            print(f'PBZ CLI v0.1.0\n')
            for name, command in self.commands.items():
                print(name)
                print(command.__doc__)
                return
        
        command_name, *invoke_args = args
        self.commands[command_name].execute(args)
