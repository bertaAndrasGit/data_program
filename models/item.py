import random
from dataclasses import dataclass, field
from functools import total_ordering
from models.model import Model
from faker import Faker

@dataclass(unsafe_hash=True)
@total_ordering
class Item(Model):
    itemid: str = field(hash=True, repr=True)
    itemname: str = field(compare=False, repr=True)
    pieces: int = field(compare=False, repr=True)
    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.itemid < other.itemid

    @staticmethod
    def generate(n: int = 10,
                 unique: bool = True,
                 different_types: list[str] = None,
                 min_pieces: int = 200, max_pieces: int = 2000) -> list:

        if different_types is None:
            different_types = ["sportcar", "tank", "boat","truck","mall","mansion","castle"]

        assert n > 0
        assert min_pieces >= 200
        assert max_pieces <= 2000
        fake = Faker()
        items = []

        for _ in range(n):
            generator = fake if not unique else fake.unique
            itemid = "toy-" + str(fake.unique.random_int(1,100))
            pieces = fake.random_int(min_pieces,max_pieces)
            items.append(Item(itemid,str(generator.country()) + "forest life" if different_types == None else random.choice(different_types) + "-lego",pieces))

        return items

if __name__ == '__main__':
    print(Item.generate(3))