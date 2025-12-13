from commands.command_context import CommandContext
from commands.enter_graph_command import EnterGraphCommand
from commands.exit_command import ExitCommand
from commands.show_adjacency_matrix import ShowAdjacencyMatrix


def main() -> None:
    context = CommandContext("Головне меню")
    context.add_command(ExitCommand())
    context.add_command(EnterGraphCommand())
    context.add_command(ShowAdjacencyMatrix())
    context.start()

if __name__ == '__main__':
    main()