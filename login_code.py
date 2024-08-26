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

def validate_new_password(password): # checks if the password is 8+ characters & contains a special character
    if (len(password) < 8) or (len(password) > 128):
        print("Password too short or too long")
        return False
    else:
        for character in password:
            if not (character.isalpha() or character.isdigit()):
                return True
        print("Doesn't contain special character")
        return False



class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_user_password(self, mydb): # saves username & password into database
        mycursor = mydb.cursor()
        save_sql = "INSERT INTO USERS (username, password) VALUES (%s, %s)"
        values = (self.username, self.password)
        mycursor.execute(save_sql, values)
        mydb.commit()

def createAccount(username, password):
    print(username, password)
    return Account(username, password)

mydb.close()