import json
import sqlite3

class Json_rw:

    @staticmethod
    def write(tablename):
        con = sqlite3.connect(r'..\..\data_program\db\storage.db')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM {tablename}")
        columns = [desc[0] for desc in cur.description]

        data = []
        for row in cur.fetchall():
            data.append(dict(zip(columns, row)))

        with open(f"{tablename}.json","w") as jsonfile:
            json.dump(data, jsonfile ,indent=4)

    @staticmethod
    def read(tablename):
        with open(f"{tablename}.json", "r") as jsonfile:
            file = json.load(jsonfile)
            print(json.dumps(file, indent=4, sort_keys=True))


##+readall +writeall


#if __name__ == '__main__':
#    code = [1,2,3]
#    name = [["a","b","c"],["d","e","f"],["g","h","i"]]
#    for na in name:
#        print(dict(zip(code,na)))


#    Json_rw.write("workers")
#    Json_rw.read("workers")