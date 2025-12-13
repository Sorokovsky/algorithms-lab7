from typing import Tuple

from graph import Graph


def generate_not_orientated_graph() -> Graph:
    vertices: list[str] = ['a', "b", "c", "d", "e", "f"]
    edges: list[Tuple[str, str]] = [
        ("a", "b"),
        ("a", "c"),
        ("a", "e"),
        ("b", "e"),
        ("b", "d"),
        ("d", "f"),
        ("d", "c"),
        ("f", "c")
    ]
    return Graph(vertices, edges, False)
