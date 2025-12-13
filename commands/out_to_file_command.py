from adjacency_list import AdjacencyList
from adjacency_matrix import AdjacencyMatrix
from commands.command import Command
from commands.command_context import CommandContext
from graph import Graph
from helpers.choosing import choose_number
from helpers.enter_graph import enter_graph


class OutToFileCommand(Command):
    def get_name(self: "OutToFileCommand") -> str:
        return "Вивести у файл"

    def execute(self: "OutToFileCommand", context: CommandContext) -> None:
        graph: Graph = context.get_graph()
        if graph is None:
            print("Граф не знайдено введіть")
            context.set_graph(enter_graph())
            graph = context.get_graph()

        file_path: str = input("Введіть назву файлу: ")
        variants: list[Graph | AdjacencyList | AdjacencyMatrix] = [AdjacencyMatrix(graph), graph, AdjacencyList(graph)]
        question: str = "Виберіть формат графа(0-Матриця суміжності, 1-Список ребер, 2-Список суміжності): "
        failure_message: str = "Відповідь не розпізнано"
        index = choose_number(question, 0, len(variants), failure_message)
        text_graph = variants[index].to_string()
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_graph)
        except FileNotFoundError:
            print("Помилка")
