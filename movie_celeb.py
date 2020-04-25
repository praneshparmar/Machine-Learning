import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="indian_movie_celebrities"

)


mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM moviecelebs")
myresult=mycursor.fetchmany(4000)

for row in myresult:
    print(row)

