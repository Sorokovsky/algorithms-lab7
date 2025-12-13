from commands.command import Command
from commands.command_context import CommandContext
from helpers.enter_graph import enter_graph


class EnterGraphCommand(Command):
    def get_name(self: "EnterGraphCommand") -> str:
        return "Ввести граф з клавіатури"

    def execute(self: "EnterGraphCommand", context: CommandContext) -> None:
        context.set_graph(enter_graph())
