from dataclasses import dataclass, field
from functools import total_ordering
from models.model import Model
from faker import Faker

@dataclass(unsafe_hash=True)
@total_ordering
class Item(Model):
    itemid: str = field(hash=True, repr=True)
    itemname: str = field(compare=False, repr=True)

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.itemid < other.itemid

    @staticmethod
    def generate(n: int = 10, unique: bool = True) -> list:

        assert n > 0

        fake = Faker()
        items = []

        for _ in range(n):
            generator = fake if not unique else fake.unique
            itemid = "toy-" + str(fake.unique.random_int(1,100))
            items.append(Item(itemid,str(generator.country()) + "-lego"))

        return items