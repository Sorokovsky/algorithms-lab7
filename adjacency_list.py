from graph import Graph


class AdjacencyList:
    _adjacency_list: dict[str, list[str]] = {}
    _is_oriented: bool

    def __init__(self: "AdjacencyList", graph: Graph) -> None:
        self._is_oriented = graph.is_oriented()
        for first, second in graph.get_edges():
            if first not in self._adjacency_list:
                self._adjacency_list[first] = []
            if second not in self._adjacency_list[first]:
                self._adjacency_list[first].append(second)
            if not self._is_oriented:
                if not second in self._adjacency_list:
                    self._adjacency_list[second] = []
                if first not in self._adjacency_list[second]:
                    self._adjacency_list[second].append(first)

    def is_oriented(self: "AdjacencyList") -> bool:
        return self._is_oriented

    def get_adjacent_list(self: "AdjacencyList") -> dict[str, list[str]]:
        keys = self._adjacency_list.keys()
        result: dict[str, list[str]] = {}
        for key in keys:
            result[key] = self._adjacency_list[key].copy()
        return result

    def print(self) -> None:
        print(self.to_string())

    def to_string(self: "AdjacencyList") -> str:
        result = ""
        open_scope: str = "{"
        close_scope: str = "}"
        i: int = 0
        for vertex in self._adjacency_list.keys():
            j: int = 0
            result += f"`{vertex}`:{open_scope} "
            for edge in self._adjacency_list[vertex]:
                result += f"`{edge}`"
                end_edge: str = ", "
                if j == len(self._adjacency_list[vertex]) - 1:
                    end_edge = ""
                result += end_edge
                j += 1
            result += close_scope
            end_vertex: str = ",\n"
            if i == len(self._adjacency_list) - 1:
                end_vertex = ""
            result += end_vertex
            i += 1
        return result
