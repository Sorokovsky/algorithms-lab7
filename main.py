from adjacency_matrix import AdjacencyMatrix
from graph import Graph
from helpers.generate_not_orientated_graph import generate_not_orientated_graph
from helpers.generate_orientated_graph import generate_orientated_graph


def main() -> None:
    not_orientated_graph: Graph = generate_not_orientated_graph()
    orientated_graph: Graph = generate_orientated_graph()
    first_matrix = AdjacencyMatrix(not_orientated_graph)
    first_matrix.print()

if __name__ == '__main__':
    main()