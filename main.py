from commands.command_context import CommandContext
from commands.enter_graph_command import EnterGraphCommand
from commands.exit_command import ExitCommand
from commands.generate_not_orientated_graph_command import GenerateNotOrientedGraphCommand
from commands.generate_orientated_graph_command import GenerateOrientedGraphCommand
from commands.show_adjacency_matrix_command import ShowAdjacencyMatrix
from commands.show_adjancency_list_command import ShowAdjacencyListCommand
from commands.show_edges_list_command import ShowEdgesListCommand


def main() -> None:
    context = CommandContext("Головне меню")
    context.add_command(ExitCommand())
    context.add_command(EnterGraphCommand())
    context.add_command(GenerateNotOrientedGraphCommand())
    context.add_command(GenerateOrientedGraphCommand())
    context.add_command(ShowAdjacencyMatrix())
    context.add_command(ShowEdgesListCommand())
    context.add_command(ShowAdjacencyListCommand())
    context.start()

if __name__ == '__main__':
    main()