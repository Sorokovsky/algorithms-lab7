from commands.command import Command
from commands.command_context import CommandContext
from helpers.generate_orientated_graph import generate_orientated_graph


class GenerateOrientedGraphCommand(Command):
    def get_name(self: "GenerateOrientedGraphCommand") -> str:
        return "Згенерувати орієнтований граф із 11 варіанту завдання"

    def execute(self: "GenerateOrientedGraphCommand", context: CommandContext) -> None:
        context.set_graph(generate_orientated_graph())
        graph = context.get_graph()
        print("Орієнтований граф")
        graph.print()
