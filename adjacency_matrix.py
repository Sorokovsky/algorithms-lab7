from typing import Tuple

from graph import Graph


class AdjacencyMatrix:
    _vertices: list[str]
    _matrix: list[list[int]]

    def __init__(self: "AdjacencyMatrix", graph: Graph) -> None:
        self._vertices = graph.get_vertices()
        self._matrix = self._get_empty_matrix(len(self._vertices))
        self._matrix = self._fill_matrix_(self._matrix, graph.get_edges())

    def _get_empty_matrix(self: "AdjacencyMatrix", size: int) -> list[list[int]]:
        matrix: list[list[int]] = []
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(0)
            matrix.append(temp)
        return matrix

    def _fill_matrix_(self: "AdjacencyMatrix", matrix: list[list[int]], edges: list[Tuple[str, str]]) -> list[
        list[int]]:
        result: list[list[int]] = [row.copy() for row in matrix]
        for first, second in edges:
            i = self._vertices.index(first)
            j = self._vertices.index(second)
            result[i][j] += 1
        return result

    def print(self: "AdjacencyMatrix") -> None:
        print(f"  ", end="")
        for vertex in self._vertices:
            print(vertex, end=" ")
        print()
        row_index = 0
        for row in self._matrix:
            print(self._vertices[row_index], *row, sep=" ")
            row_index += 1
