from adjacency_list import AdjacencyList
from commands.command import Command
from commands.command_context import CommandContext
from graph import Graph
from helpers.parse_graph_from_string_matrix import parse_graph_from_matrix


class ShowAdjacencyListFromMatrixFileCommand(Command):
    def get_name(self: "ShowAdjacencyListFromMatrixFileCommand") -> str:
        return "Побудувати список суміжності із матриці суміжності(файлу)"

    def execute(self: "ShowAdjacencyListFromMatrixFileCommand", context: CommandContext) -> None:
        file_name: str = input("Введіть назву файлу: ")
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                matrix_string: str = file.read()
                context.set_graph(parse_graph_from_matrix(matrix_string))
                graph: Graph = context.get_graph()
                print("Список суміжності: ")
                AdjacencyList(graph).print()
        except FileNotFoundError:
            print("Файл не знайдено")
