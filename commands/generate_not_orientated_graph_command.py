from commands.command import Command
from commands.command_context import CommandContext
from helpers.generate_not_orientated_graph import generate_not_orientated_graph


class GenerateNotOrientedGraphCommand(Command):
    def get_name(self: "GenerateNotOrientedGraphCommand") -> str:
        return "Згенерувати неорієнтований граф із 11 варіанту завдання"

    def execute(self: "GenerateNotOrientedGraphCommand", context: CommandContext) -> None:
        context.set_graph(generate_not_orientated_graph())
        graph = context.get_graph()
        print("Неорієнтований граф")
        graph.print()
