import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person1:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    # 1 - Fix to make it print correctly
    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


# 2 - This does the same as above, just slight different return
@dataclass(slots=True)
class Person2:
    name: str
    address: str
    active: bool = True
    # 3 - If you provide a default value array then it is all the same array, so you do this
    contact_methods: list[str] = field(default_factory=list)
    # Can not provide ID
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person2(name="John", address="123 Main St")
    print(person)
