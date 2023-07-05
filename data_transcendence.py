import pandas as pd
import mysql.connector

excel_file = 'Book 1.xlsx'
df = pd.read_excel(excel_file)

with open('excel.py','a') as f:
    content = f.write('''
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="excel"
)\n''')

    content2 = f.write("cursor = conn.cursor()\n")

for index, row in df.iterrows():

    with open('excel.py','a') as f:
        content3 = f.write(f'''query = "INSERT INTO Excel (id, username, name, password) VALUES (%s,%s,%s,%s)"
cursor.execute(query, ("{row[0]}", "{row[1]}","{row[2]}","{row[3]}"))
conn.commit()\n''')
print("Behold! An exquisite masterpiece has been born—an impeccably crafted Python script, meticulously generated with resounding success!")
