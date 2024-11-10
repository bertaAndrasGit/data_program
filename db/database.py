import sqlite3

from models.storage import Storage
from models.worker import Worker
from models.item import Item

class Database:




    @staticmethod
    def _connect_database():
        storage = r'..\beadando\db\storage.db'
        con = sqlite3.connect(storage)  # ':memory:'
        cur = con.cursor()

        return con, cur

    @staticmethod
    def _close_database(con,cur):
        con.commit()
        cur.close()
        con.close()


    def create(self) -> None:
        con, cur = self._connect_database()

        #create workers table
        cur.execute("CREATE TABLE IF NOT EXISTS workers(workcode INTEGER(5) PRIMARY KEY NOT NULL, "
                                                        "name VARCHAR(30) not null, "
                                                        "jobtitle VARCHAR(30), "
                                                        "male BOOLEAN, "
                                                        "phonenumber VARCHAR(50) )")
        #create items table
        cur.execute("CREATE TABLE IF NOT EXISTS items(itemid VARCHAR(10) PRIMARY KEY NOT NULL,"
                                                        "itemname VARCHAR(50), "
                                                        "pieces INTEGER(5) )")
        #create storages table
        cur.execute("CREATE TABLE IF NOT EXISTS storages(id INTEGER(5) PRIMARY KEY NOT NULL, "
                                                        "itemid VARCHAR(10),"
                                                        "stock INTEGER(5), "
                                                        "price FLOAT(10), "
                                                        "FOREIGN KEY (itemid) REFERENCES items(itemid) )")
        #create log table
        cur.execute("CREATE TABLE IF NOT EXISTS log(workcode INTEGER(5),"
                                                    "storageid INTEGER(5),"
                                                    "itemid VARCHAR(10),"
                                                    "quantity INTEGER(5),"
                                                    "FOREIGN KEY (workcode) REFERENCES workers(workcode),"
                                                    "FOREIGN KEY (storageid) REFERENCES storages(id) )")

        self._close_database(con,cur)



    def load_up_workers(self,*args,**kwargs) -> None:
        con, cur = self._connect_database()

        workers = Worker.generate(*args,**kwargs)
        worker_data = [(worker.workcode, worker.name, worker.jobtitle, worker.male, worker.phonenumber) for worker in
                       workers]
        try:
            cur.executemany("INSERT INTO workers VALUES (?, ?, ?, ?, ?)", worker_data)
        except sqlite3.IntegrityError:
            pass

        self._close_database(con, cur)

    def load_up_items(self, *args, **kwargs) -> None:
        con, cur = self._connect_database()

        items = Item.generate(*args, **kwargs)
        item_data = [(item.itemid, item.itemname) for item in items]
        try:
            cur.executemany("INSERT INTO items VALUES (?, ?, ?)", item_data)
        except sqlite3.IntegrityError:
            pass

        self._close_database(con, cur)

    def load_up_storages(self, *args, **kwargs) -> None:
        con, cur = self._connect_database()

        storages = Storage.generate(*args, **kwargs)
        storage_data = [(storage.id, storage.itemid, storage.stock, storage.price) for storage in storages]
        try:
            cur.executemany("INSERT INTO storages VALUES (?, ?, ?, ?)", storage_data)
        except sqlite3.IntegrityError:
            pass

        self._close_database(con, cur)

    def load_up(self,table_name,entity,columns:list,*args,**kwargs):
        con,cur = self._connect_database()

        generate = entity.generate(*args,**kwargs)
        items = [tuple(getattr(item,column) for column in columns) for item in generate]
        print(items)
        values = ", ".join("?" * len(columns))
        sql = f"INSERT INTO {table_name} VALUES ({values})"

        try:
            cur.executemany(sql,items)
        except sqlite3.IntegrityError:
            pass

        self._close_database(con,cur)
