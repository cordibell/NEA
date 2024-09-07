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

class LoginCommands: # encapsulates methods to collect & process data from login menu
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

class JoinEventCommands: # encapsulates methods to collect & process data from join event menu
    def __init__(self, mydb):
        self.mydb = mydb
    
    def set_join_event(self, join_event):
        self.join_event = join_event
        
    def collect_join_event(self): # collects data from join event code text field
        pass
    
    def collect_host_event(self): # collects data from hosting event inputs
        selected_timeframe = self.join_event.get_timeframe_var()
        timeframe = join_events_code.find_timeframe(selected_timeframe)
        start_date = self.join_event.get_start_date()
        end_date = self.join_event.get_end_date()
        event_name = self.join_event.get_event_title()
        join_events_code.host_event(event_name, timeframe, start_date, end_date)  

if __name__ == '__main__':
    loginCommand = LoginCommands(mydb)
    login = login_gui.login_menu(loginCommand.collect_login, loginCommand.collect_new_account)
    loginCommand.set_login(login)
    joinEventCommand = JoinEventCommands(mydb)
    join_event = join_events.join_events_menu(login.login_window, joinEventCommand.collect_join_event, joinEventCommand.collect_host_event)
    joinEventCommand.set_join_event(join_event)
    # join_event.join_events_window.withdraw()
    login.login_window.mainloop()

