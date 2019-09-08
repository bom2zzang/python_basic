#!/usr/bin/env python3 
import sqlite3
#DB를 생성하고 4개의 속성을 가진 SALES 테이블을 생성한다.

con = sqlite3.connect(':memory:')
#con = sqlite3.connect('d:/python3/0908/new_db.sql)
query = """CREATE TABLE SALES (
    customer VARCHAR(20)
    ,product VARCHAR(40)
    ,amount FLOAT
    ,date DATE);"""

con.execute(query)
con.commit()

#SALES 테이블에 데이터 삽입
data = [('Richard Lucas','Notepad',2.50,'2019-05-01')
        ,('Janny Kim','Binder',4.15,'2019-06-06')
        ,('Xiumin','Printer',155.75,'2019-07-07')
        ,('MS Kim','Computer',679,'2019-08-08')]
statement = "INSERT INTO SALES VALUES(?,?,?,?)"
con.executemany(statement,data)
con.commit()

#SASLES 테이블에 질의하기
cursor = con.execute("select * from sales")
rows = cursor.fetchall()

#출력된 데이터의 수를 센다.
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print()
print("Number of rows")
print(row_counter)