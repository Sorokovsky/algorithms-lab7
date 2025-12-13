from typing import Tuple

from graph import Graph


def generate_orientated_graph() -> Graph:
    vertices: list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
    edges: list[Tuple[str, str]] = [
        ('a', 'b'),
        ('a', 'e'),
        ('e', 'a'),
        ('b', "a"),
        ('a', 'c'),
        ('b', 'c'),
        ('b', 'f'),
        ('f', 'b'),
        ('e', 'd'),
        ('e', 'f'),
        ('f', 'd')
    ]
    return Graph(vertices, edges, True)
