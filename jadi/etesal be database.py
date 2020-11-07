import mysql.connector

cnx = mysql.connector.connect(user='root', password='alireza',  # create connection va store mikone ru in variable
                              host='localhost:3306',
                              database='learn')

# a har kari mikhaym ine ke ru in variable bokonim
cnx.close()
