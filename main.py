from models.worker import Worker
from db.database import Database
from models.item import Item
from models.storage import Storage
def main() -> None:

    storagepath = r"..\data_program\db\storage.db"
    db = Database(storagepath)
    db.create()

    db.load_up("workers",Worker,
               ["workcode","name","jobtitle","male","phonenumber"],
               10, unique=True, min_age=18, max_age=65)
    db.load_up("items",Item,
               ["itemid","itemname"],
               20)
    db.load_up("storages",Storage,
               ["id","itemid","stock","price"],
               5)

if __name__ == '__main__':
    main()