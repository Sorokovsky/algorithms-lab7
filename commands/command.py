from abc import ABC, abstractmethod


class Command(ABC):
    _id: int

    def get_id(self: "Command") -> int:
        return self._id

    def set_id(self: "Command", value: int) -> None:
        self._id = value

    @abstractmethod
    def get_name(self: "Command") -> str:
        pass

    @abstractmethod
    def execute(self, context: "CommandContext") -> None:
        pass
