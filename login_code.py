# login code
import tkinter as Tk
import mysql.connector 

# Setting up database
mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

print(mydb)
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        print("Saving object to database")

def createAccount(username, password):
    print(username, password)
    return Account(username, password)

mydb.close()