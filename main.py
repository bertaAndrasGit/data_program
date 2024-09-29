import sqlite3

from db.database import Database
def main() -> None:
    storagepath = r"C:\Users\Andras\PycharmProjects\beadando\db\storage.db"
    db = Database(storagepath)
    db.create()
    db.load_up_workers()
    db.load_up_items()
    db.load_up_storages()

if __name__ == '__main__':
    main()