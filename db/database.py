import sqlite3

class Database:

    def __init__(self, storagepath):
        self.storagepath = storagepath

    @staticmethod
    def _connect_database():
        storage = r'..\data_program\db\storage.db'  # N:M
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
                                                        "itemname VARCHAR(50) )")
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


    def load_up(self,table_name,method,columns:list,*args,**kwargs):
        con,cur = self._connect_database()

        generate = method.generate(*args,**kwargs)
        items = [tuple(getattr(item,column) for column in columns) for item in generate]
        values = ", ".join("?" * len(columns))
        sql = f"INSERT INTO {table_name} VALUES ({values})"


        try:
            cur.executemany(sql,items)
        except sqlite3.IntegrityError:
            pass

        self._close_database(con,cur)

