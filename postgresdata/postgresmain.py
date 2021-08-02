import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='and_database' user='postgres'  password='Kangher115!' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mystore (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert_table(quantity, price,item):
    conn = psycopg2.connect("dbname='and_database' user='postgres'  password='Kangher115!' host='localhost' port='5432' ")
    cur = conn.cursor()
    # cur.execute("INSERT INTO mystore VALUES('%s','%s','%s')" % (item, quantity, price)) sql injection
    cur.execute("INSERT INTO mystore VALUES(%s,%s,%s)", (quantity, price,item))
    conn.commit()
    conn.close()


def view():

    conn = psycopg2.connect("dbname='and_database' user='postgres'  password='Kangher115!' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mystore")
    data = cur.fetchall()
    return data
    conn.close


def delete(item):

    conn = psycopg2.connect("dbname='and_database' user='postgres' password='Kangher115!' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM mystore WHERE item= %s ",(item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):

    conn = psycopg2.connect("dbname='and_database' user='postgres' password='Kangher115!' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE mystore SET quantity=%s,price=%s WHERE item = %s", (quantity, price,item))
    conn.commit()
    conn.close

create_table()
# insert_table("coffee cub", 10,5)
# insert_table("cream", 3,5)
# insert_table("beer", 4,6)
# insert_table("Icecream", 3,5)
# insert_table("IceTea", 2,1)
# insert_table("Banana", 2,1)
# insert_table("Cofee", 2,1)
update("coffee cub",1,7,)
# delete('Cofee')
print(view())

# import psycopg2
# conn= psycopg2.connect(database="suppliers" ,user="postgres", password="Kangher115!",host="localhost",port="5432")
# cur=conn.cursor()
# cur.execute("""
# CREATE TABLE COMPA
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);
# """)
# print("Table is created")
# conn.commit()
# conn.close()