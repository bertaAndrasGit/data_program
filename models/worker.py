import random
from dataclasses import dataclass, field
from functools import total_ordering
from faker import Faker
from models.model import Model


@dataclass(unsafe_hash=True)
@total_ordering
class Worker(Model):
    workcode: int = field(hash=True)
    name: str = field(compare=False)
    jobtitle: str = field(compare=False)
    male: bool = field(compare=False)
    phonenumber: str = field(compare=False)

    def __lt__(self, other):
        if not isinstance(other, Worker):
            return NotImplemented
        return self.workcode < other.workcode

    @staticmethod
    def generate(n: int = 10, locale: str = "en_US", unique: bool = True, min_age: int = 18, max_age: int = 65) -> list:

        assert n > 0
        assert min_age >= 18

        fake = Faker(locale)
        workers = []
        job_titles = ["Assistant","Cashier","Team Leader","Inventory Control Specialist","Sales Manager","Logistics","Warehouse Associate"]
        for _ in range(n):
            male = random.random() < 0.5
            generator = fake if not unique else fake.unique
            workers.append(
                            Worker( fake.unique.random_int(10000,99999),
                                    generator.name_female() if not male else generator.name_male(),
                                    random.choice(job_titles),
                                    male,
                                    generator.phone_number()
                            )
            )

        return workers
