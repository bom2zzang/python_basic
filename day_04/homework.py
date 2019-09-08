import csv
import pymysql
import sys

# Path to and name of a CSV output file
output_file = sys.argv[1]
data = sys.argv[2]

print(data)
# Connect to a MySQL database
con = pymysql.connect(host='localhost', port=3306, db='studydb', user='root', passwd='1111')
c = con.cursor()

# Create a file writer object and write the header row
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['bno','title','conts','file','date']
filewriter.writerow(header)

statement = "SELECT * FROM BOARD WHERE title like concat('%%',%s,'%%')"
c.executemany(statement, data)

rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
 
 #cmd>python3 homework.py hie.csv 제 > where title search
 #참고 : https://stackoverflow.com/questions/18002643/valueerror-unsupported-format-character-0x22-at-in-python-string