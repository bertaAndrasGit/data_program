import csv
import sqlite3

class Csv_rw:

    @staticmethod
    def write(tablename):
        con = sqlite3.connect(r'..\..\beadando\db\storage.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {tablename}")
        columns = [desc[0] for desc in cur.description]

        with open(f'{tablename}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            writer.writerow(columns)
            for data in cur.fetchall():
                writer.writerow(data)

        cur.close()
        con.close()



    @staticmethod
    def read(tablename):
        with open(f'{tablename}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                print(', '.join(row))







if __name__ == '__main__':
    Csv_rw.write("workers")
    Csv_rw.read("workers")
    print("-----------------------")
    Csv_rw.write("items")
    Csv_rw.read("items")
    print("-----------------------")
    Csv_rw.write("storages")
    Csv_rw.read("storages")