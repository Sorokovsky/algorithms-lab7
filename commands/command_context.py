from commands.command import Command
from helpers.choosing import choose_number


class CommandContext:
    _commands: list[Command] = []
    _title: str
    _is_running: bool = False

    def __init__(self: "CommandContext", title: str) -> None:
        self._title = title

    def add_command(self: "CommandContext", command: Command) -> None:
        self._commands.append(command)

    def start(self: "CommandContext") -> None:
        self._is_running = True
        self._loop()

    def exit(self: "CommandContext") -> None:
        self._is_running = False
        self._prepare_command()
        self._loop()

    def _loop(self: "CommandContext") -> None:
        while self._is_running:
            self._show_commands()
            command = self._choose_command()
            command.execute(self)

    def _prepare_command(self: "CommandContext") -> None:
        current_id: int = 0
        for command in self._commands:
            command.set_id(current_id)
            current_id += 1

    def _choose_command(self: "CommandContext") -> Command:
        command_id: int = choose_number(">> ", 0, len(self._commands) - 1, "Команду не розпізнано.")
        return self._commands[command_id]

    def _show_commands(self: "CommandContext") -> None:
        print(self._title)
        for command in self._commands:
            print(f"{command.get_id()}-{command.get_name()}.")
