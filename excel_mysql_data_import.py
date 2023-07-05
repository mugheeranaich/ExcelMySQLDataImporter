import pandas as pd
import mysql.connector
from tabulate import tabulate


excel_file = 'file:///home/mugheera/excel_mySQL/Book 1.xlsx'
df = pd.read_excel(excel_file)
data = []

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="excel"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Excel")

for index, row in df.iterrows():
    query = "INSERT INTO Excel (id, username, name, password) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (row[0], row[1],row[2],row[3]))
    conn.commit()

cursor.execute("SELECT * FROM Excel")

myresult = cursor.fetchall()

data=[]
for x in myresult:
    x=list(x)
    data.append(x)
table = tabulate(data, headers=["id","username","name","password"], tablefmt="fancy_grid")
print(table)
