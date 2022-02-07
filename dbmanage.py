import  sqlite3

connection = sqlite3.connect("wallet.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO transactions VALUES('1','money','description', '500', '50', '2006-01-05', 'c7fd1b04-4516-419a-a9f5-acd960af4474', '870ff42d-62e0-4fda-8b29-39958418fd81')")

connection.commit()