import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert_table(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():

    conn = sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT *FROM store")
    data = cur.fetchall()
    return data
    conn.close

create_table()
insert_table("Water Glass", 10 ,5)
insert_table("Shaver", 15 ,4)
print(view())