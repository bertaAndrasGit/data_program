import json
import sqlite3

from models.item import Item
from models.worker import Worker
from models.storage import Storage

class Json_rw:

    @staticmethod
    def write(tablename):
        con = sqlite3.connect(r'..\..\beadando\db\storage.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {tablename}")
        columns = [desc[0] for desc in cur.description]
        data = []

        for row in cur.fetchall():
            data.append(dict(zip(columns, row)))

        with open(f"{tablename}.json","w") as jsonfile:
            json.dump(data, jsonfile ,indent=4)

        cur.close()
        con.close()

    @staticmethod
    def read(tablename,entity):
        with open(f"{tablename}.json", "r") as jsonfile:
            #file = json.load(jsonfile)
            #print(json.dumps(file, indent=4, sort_keys=True))
            return json.load(jsonfile,object_hook=lambda d: entity(**d))




if __name__ == '__main__':
#    code = [1,2,3]
#    name = [["a","b","c"],["d","e","f"],["g","h","i"]]
#    for na in name:
#        print(dict(zip(code,na)))


    Json_rw.write("workers")
    print(Json_rw.read("workers",Worker))
    print("-----------------------")
    Json_rw.write("items")
    print(Json_rw.read("items",Item))
    print("-----------------------")
    Json_rw.write("storages")
    print(Json_rw.read("storages",Storage))