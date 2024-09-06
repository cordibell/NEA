# main file, made 5/9/24

import login_gui
import login_code
import join_events
import join_events_code
import mysql.connector

# connecting to database

mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)


# logging in

class LoginCommands:
    def __init__(self, mydb):
        self.mydb = mydb

    def set_login(self, login):
        self.login = login 

    def collect_login(self): # collects data from login to existing account text fields
        username = self.login.get_existing_username()
        password = self.login.get_existing_password()
        login_code.validate_login(username, password, self.mydb)
    
    def collect_new_account(self): # collects data from new account text fields
        username = self.login.get_new_username()
        password = self.login.get_new_password()
        login_code.saving_new_account(username, password, self.mydb)

    

if __name__ == '__main__':
    command = LoginCommands(mydb)
    login = login_gui.login_menu(command.collect_login, command.collect_new_account)
    command.set_login(login)
    login.login_window.mainloop()



#join_events_window = join_events.join_events_menu(login_window)

