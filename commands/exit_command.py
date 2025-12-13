from commands.command import Command
from commands.command_context import CommandContext


class ExitCommand(Command):
    def get_name(self: "Command") -> str:
        return "Вихід"

    def execute(self: "ExitCommand", context: CommandContext) -> None:
        context.exit()
