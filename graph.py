from typing import Tuple

class Graph:
    _vertices: list[str] = []
    _edges: list[Tuple[str, str]] = []
    _is_orientated: bool

    def __init__(self: "Graph", vertices: list[str], edges: list[tuple[str, str]], is_orientated: bool = False) -> None:
        for first, second in edges:
            if first not in vertices or second not in vertices:
                raise ValueError(f"{first} або {second} не є вершиною графа, тому не може бути ребром")

        self._edges = edges
        self._is_orientated = is_orientated
        self._vertices = vertices

    def is_oriented(self: "Graph") -> bool:
        return self._is_orientated

    def get_vertices(self: "Graph") -> list[str]:
        return self._vertices.copy()

    def get_edges(self: "Graph") -> list[tuple[str, str]]:
        return self._edges.copy()

    def print(self: "Graph") -> None:
        print("Graph: ")
        seperator = ";"
        for first, second in self._edges:
            print(f"({first}{seperator}{second})")
