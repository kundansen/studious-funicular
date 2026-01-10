from abc import ABC, abstractmethod
from typing import Any, Dict

class Agent(ABC):
    """Base class for blog agents.

    Agents implement a simple `run` method that receives a dict of inputs
    and returns a dict of outputs. Keep them stateless where possible.
    """

    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent task."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Agent {self.name}>"
