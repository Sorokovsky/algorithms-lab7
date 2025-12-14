from typing import Tuple

from graph import Graph


def prepare_matrix_end_vertices(string_matrix: str) -> Tuple[list[str], list[list[int]]]:
    matrix: list[list[int]] = []
    vertices: list[str] = []
    line_index: int = 0
    for line in string_matrix.splitlines():
        temp: list[int] = []
        for char in line.split():
            try:
                temp.append(int(char))
            except ValueError:
                if line_index == 0:
                    vertices.append(char)
        if line_index != 0:
            matrix.append(temp)
        line_index += 1
    return vertices, matrix


def is_graph_orientated_by_matrix(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            first = matrix[i][j]
            second = matrix[j][i]
            if first != second:
                return True
    return False


def parse_edges(matrix: list[list[int]], vertices: list[str]) -> list[Tuple[str, str]]:
    result: list[tuple[str, str]] = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            first_vertex: str = vertices[i]
            second_vertex: str = vertices[j]
            if matrix[i][j] == 1:
                result.append((first_vertex, second_vertex))
    return result


def parse_graph_from_matrix(string_matrix: str) -> Graph:
    vertices, matrix = prepare_matrix_end_vertices(string_matrix)
    edges: list[Tuple[str, str]] = parse_edges(matrix, vertices)
    is_orientated: bool = is_graph_orientated_by_matrix(matrix)
    return Graph(vertices, edges, is_orientated)
