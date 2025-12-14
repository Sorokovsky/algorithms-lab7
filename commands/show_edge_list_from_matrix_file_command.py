from commands.command import Command
from commands.command_context import CommandContext
from helpers.parse_graph_from_string_matrix import parse_graph_from_matrix


class ShowEdgeListFromMatrixFileCommand(Command):
    def get_name(self: "ShowEdgeListFromMatrixFileCommand") -> str:
        return "Побудувати список ребер із матриці суміжності(файлу)"

    def execute(self: "ShowEdgeListFromMatrixFileCommand", context: CommandContext) -> None:
        file_name = input("Введіть назву файлу: ")
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                matrix_string: str = file.read()
                context.set_graph(parse_graph_from_matrix(matrix_string))
                graph = context.get_graph()
                print("Список ребер")
                graph.print()
        except FileNotFoundError:
            print("Файл не знайдено")
