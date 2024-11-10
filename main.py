from models.worker import Worker
from db.database import Database
from models.item import Item
from models.storage import Storage
def main() -> None:

    db = Database()
    db.create()

    db.load_up("workers",Worker,
               ["workcode","name","jobtitle","male","phonenumber"],
               1, unique=True, min_age=18, max_age=65)

    db.load_up("items", Item,
               ["itemid", "itemname", "pieces"],
               1)
    db.load_up("storages", Storage,
               ["id", "itemid", "stock", "price"],
               1)


if __name__ == '__main__':
    main()