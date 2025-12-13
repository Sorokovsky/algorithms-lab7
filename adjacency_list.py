from graph import Graph


class AdjacencyList:
    _adjacency_list: dict[str, list[str]] = {}
    _is_oriented: bool

    def __init__(self: "AdjacencyList", graph: Graph) -> None:
        self._is_oriented = graph.is_oriented()
        for first, second in graph.get_edges():
            if first not in self._adjacency_list:
                self._adjacency_list[first] = []
            self._adjacency_list[first].append(second)

    def is_oriented(self: "AdjacencyList") -> bool:
        return self._is_oriented

    def get_adjacent_list(self: "AdjacencyList") -> dict[str, list[str]]:
        keys = self._adjacency_list.keys()
        result: dict[str, list[str]] = {}
        for key in keys:
            result[key] = self._adjacency_list[key].copy()
        return result

    def print(self) -> None:
        key_index = 0
        for key, value in self._adjacency_list.items():
            print(f"`{key}`: ", "{ ", sep="", end="")
            for i in range(len(value)):
                row = value[i]
                end = ", "
                if i == len(value) - 1:
                    end = " "
                print(f"`{row}`{end}", sep="", end="")
            key_end = ","
            if key_index == len(self._adjacency_list.items()) - 1:
                key_end = ""
            print("}", key_end, sep="")
            key_index += 1
