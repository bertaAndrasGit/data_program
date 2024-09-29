from dataclasses import dataclass, field
from functools import total_ordering
from models.model import Model
from faker import Faker
from models.item import Item
import random
@dataclass(unsafe_hash=True)
@total_ordering
class Storage(Model):
    id: int = field(hash=True)
    itemid: str = field(compare=False)
    stock: int = field(compare=False)
    price: float = field(compare=False)


    def __lt__(self, other):
        if not isinstance(other, Storage):
            return NotImplemented
        return self.id < other.id

    @staticmethod
    def generate(n: int = 5, locale: str = "en_US",
                 min_price:float = 5.95, max_price:float = 200.99,
                 min_stock:int = 0, max_stock:int = 100) -> list:

        assert n > 0
        assert max_price > min_price > 0


        storages = []
        fake = Faker()

        itemids = [item.itemid for item in Item.generate(n)]
        for _ in range(n):
            storages.append(Storage(fake.random_int(1,999),
                                    str(*random.choices(itemids)),
                                    fake.random_int(min_stock,max_stock),
                                    round(random.uniform(min_price,max_price),2))
                            )

        return storages