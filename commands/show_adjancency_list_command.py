from adjacency_list import AdjacencyList
from commands.command import Command
from commands.command_context import CommandContext
from helpers.enter_graph import enter_graph


class ShowAdjacencyListCommand(Command):
    def get_name(self: "ShowAdjacencyListCommand") -> str:
        return "Показати список суміжності"

    def execute(self: "ShowAdjacencyListCommand", context: CommandContext) -> None:
        graph = context.get_graph()
        if graph is None:
            print("Граф не знайдено, введіть.")
            context.set_graph(enter_graph())
            graph = context.get_graph()
        print("Список суміжності")
        adjacency_list = AdjacencyList(graph)
        adjacency_list.print()
