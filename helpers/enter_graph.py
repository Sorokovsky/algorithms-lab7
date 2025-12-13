from typing import Tuple

from graph import Graph
from helpers.choosing import choose_number, choose_binary


def enter_graph() -> Graph:
    is_orientated: bool = choose_binary("Граф орієнтований?")
    vertices_count = choose_number("Введіть кількість вершин: ", 0, None, "Кількість вершин не може бути від'ємною.")
    vertices: list[str] = []
    for i in range(vertices_count):
        vertices.append(input(f"Введіть {i + 1}-й вершину: "))
    edge_count: int = choose_number("Введіть кількість ребер графа: ", 0, None,
                                    "Кількість ребер не може бути від'ємною.")
    edges: list[Tuple[str, str]] = []
    for i in range(edge_count):
        print(f"{i + 1}-е ребро")
        first = input("Введіть першу вершину: ")
        while first not in vertices:
            first = input("Це не вершина. Спробуйте ще: ")
        second = input("Введіть другу вершину: ")
        while second not in vertices:
            second = input("Це не вершина. Спробуйте ще: ")
        edges.append((first, second))
    return Graph(vertices, edges, is_orientated)
