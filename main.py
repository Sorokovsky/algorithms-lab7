from commands.command_context import CommandContext
from commands.exit_command import ExitCommand


def main() -> None:
    context = CommandContext("Головне меню")
    context.add_command(ExitCommand())
    context.start()

if __name__ == '__main__':
    main()