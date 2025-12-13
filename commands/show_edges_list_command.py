from commands.command import Command
from commands.command_context import CommandContext
from helpers.enter_graph import enter_graph


class ShowEdgesListCommand(Command):
    def get_name(self: "ShowEdgesListCommand") -> str:
        return "Вивести список ребер."

    def execute(self: "ShowEdgesListCommand", context: CommandContext) -> None:
        graph = context.get_graph()
        if graph is None:
            print("Граф не знайдено, введіть.")
            context.set_graph(enter_graph())
            graph = context.get_graph()
        print("Список ребер")
        graph.print()
