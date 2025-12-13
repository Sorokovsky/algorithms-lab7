from adjacency_matrix import AdjacencyMatrix
from commands.command import Command
from commands.command_context import CommandContext
from helpers.enter_graph import enter_graph


class ShowAdjacencyMatrix(Command):
    def get_name(self: "ShowAdjacencyMatrix") -> str:
        return "Показати граф матрицею суміжності"

    def execute(self: "ShowAdjacencyMatrix", context: CommandContext) -> None:
        graph = context.get_graph()
        if graph is None:
            print("Графу не знайдено. Введіть граф.")
            context.set_graph(enter_graph())
            graph = context.get_graph()
        matrix = AdjacencyMatrix(graph)
        print("Матриця суміжності")
        matrix.print()
