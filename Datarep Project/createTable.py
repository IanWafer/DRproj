import mysql.connector
import dbconfig as cfg

# Set up connection to database
db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()

# Create table for storage of information
sql='CREATE TABLE santaPresents (id INT PRIMARY KEY, name VARCHAR(250), fromAge INT, price INT)'

cursor.execute(sql)