import csv
import sqlite3
import sys

input_file = sys.argv[1]

con = sqlite3.connect('SUBWAY.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS SUBWAY 
                                (ID VARCHAR(20)
                                ,Station VARCHAR(20)
                                ,Weekday VARCHAR(20)
                                ,Saturday VARCHAR(20)
                                ,Sunday VARCHAR(20));"""
c.execute(create_table)
con.commit()

file_reader = csv.reader(open(input_file, 'r', encoding='UTF8'), delimiter = ',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
            data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO SUBWAY VALUES(?, ?, ?, ?, ?);", data)
con.commit()

output = c.execute("SELECT * FROM SUBWAY")
rows = output.fetchall()
for row in rows:
    output = [] 
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)

# cmd > python sql3.py subway.csv 