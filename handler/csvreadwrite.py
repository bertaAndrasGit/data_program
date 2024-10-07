import csv
import sqlite3

class Csv_rw:

    @staticmethod
    def write(tablename):

        con = sqlite3.connect(r'..\..\data_program\db\storage.db')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM {tablename}")
        columns = [desc[0] for desc in cur.description]

        with open(f'{tablename}.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            spamwriter.writerow(columns)
            for data in cur.fetchall():
                spamwriter.writerow(data)

        con.close()
        cur.close()


    @staticmethod
    def read(tablename):
        with open(f'{tablename}.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                print(', '.join(row))


##+readall +writeall




#if __name__ == '__main__':
#    Csv_rw.write("workers")
#    Csv_rw.read("workers")