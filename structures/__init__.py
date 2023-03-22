import dataclasses


@dataclasses.dataclass
class Item:
    name: str = ""
    price: float = ""


@dataclasses.dataclass
class Recipe:
    name: str = ""
    cost: float = 0
    num_of_trades: float = 0
    value: float = 0
