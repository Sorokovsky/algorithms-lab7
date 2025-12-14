from adjacency_list import AdjacencyList
from commands.command import Command
from commands.command_context import CommandContext
from helpers.enter_graph import enter_graph


class DepthFirstSearchCommand(Command):
    def get_name(self: "DepthFirstSearchCommand") -> str:
        return "Обхід в глибину на стеку"

    def execute(self: "DepthFirstSearchCommand", context: CommandContext) -> None:
        graph = context.get_graph()
        if graph is None:
            print("Графа не знайдено, введіть.")
            context.set_graph(enter_graph())
            graph = context.get_graph()
        dfs_lookup = self.dfs(None, AdjacencyList(graph), [])
        print("Обхід в глибину")
        while len(dfs_lookup) > 0:
            print(dfs_lookup.pop())

    def dfs(self: "DepthFirstSearchCommand", vertex: str | None, adjacency_list: AdjacencyList, used: list[str]) -> \
    list[str]:
        new_used: list[str] = used.copy()
        adjacency = adjacency_list.get_adjacent_list()
        new_vertex = vertex
        if new_vertex is None:
            new_vertex = sorted(adjacency.keys())[0]
        new_used.append(new_vertex)
        if new_vertex in adjacency.keys():
            for neighbour in adjacency[new_vertex]:
                if neighbour not in new_used:
                    new_used = self.dfs(neighbour, adjacency_list, new_used)
        return new_used
