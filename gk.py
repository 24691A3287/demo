import psycopg2
con=psycopg2.connect(database="vasu",host="localhost",password="delab",user="postgres",port="5432")
cur=con.cursor()
print("successfully connected")


cur.execute(""" select m.name, mo.roll from m inner join mo on m.id=mo.id""");
for row in cur.fetchall():
    print(row)
con.commit()
