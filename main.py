# main file, made 5/9/24

import login_gui
import login_code

import join_events_gui
import join_events_code

import calendar_gui

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
        self.is_logged_in = False

    def set_login(self, login):
        self.login = login 

    def collect_login(self): # collects data from login to existing account text fields
        self.existing_username = self.login.get_existing_username()
        self.existing_password = self.login.get_existing_password()
        self.is_logged_in = login_code.validate_login(self.existing_username, self.existing_password, self.mydb)
        if self.is_logged_in == True:
            self.load_join_menu()
    
    def load_join_menu(self): # loads next menu if username matches password & withdraws current menu
        joinEventCommand = JoinEventCommands(mydb)
        self.login.login_window.withdraw()
        join_event = join_events_gui.join_events_menu(login.login_window, joinEventCommand.collect_join_event, joinEventCommand.collect_host_event)
        joinEventCommand.set_join_event(join_event)

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
        eventID = self.join_event.get_join_event_code()
        id_exists = join_events_code.find_event_id(eventID, self.mydb)
        if id_exists:
            self.load_calendar_menu()
        
    def collect_host_event(self): # collects data from hosting event inputs
        selected_timeframe = self.join_event.get_timeframe_var()
        timeframe = join_events_code.find_timeframe(selected_timeframe)
        start_date = self.join_event.get_start_date()
        end_date = self.join_event.get_end_date()
        event_name = self.join_event.get_event_title()
        generated_code = join_events_code.generate_unique_code(self.mydb)
        valid_event = join_events_code.host_event(event_name, timeframe, start_date, end_date, generated_code, login.get_existing_username(), self.mydb)  
        if valid_event:
            self.join_event.display_unique_code(generated_code)

    def load_calendar_menu(self): # loads the calendar menu & hides join event menu
        calendarCommand = CalendarCommands(self.mydb)
        self.join_event.join_events_window.withdraw()
        calendar_menu = calendar_gui.calendar_menu(login.login_window)
        calendarCommand.set_calendar_menu(calendar_menu)

class CalendarCommands:
    def __init__(self, mydb):
        self.mydb = mydb

    def set_calendar_menu(self, calendar_menu):
        self.calendar_menu = calendar_menu

if __name__ == '__main__':
    loginCommand = LoginCommands(mydb)
    login = login_gui.login_menu(loginCommand.collect_login, loginCommand.collect_new_account)
    loginCommand.set_login(login)

    # join_event.join_events_window.withdraw()
    login.login_window.mainloop()
