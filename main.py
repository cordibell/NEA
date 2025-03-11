# main file, made 5/9/24

# importing other modules 
import login_gui
import login_code

import join_events_gui
import join_events_code

import calendar_gui

import create_event_gui
import create_event_code

import set_preferred_time_gui
import set_preferred_times_code

import optimal_time_gui
import calculate_optimal_time

import mysql.connector

# connecting to database using mysql connector library

mydb = mysql.connector.connect(
    host="10.0.2.214",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)


# logging in commands

class LoginCommands: # encapsulates methods to collect & process data from login menu
    '''
    This class encapsulates everything to do with the login page, such as the window & its functionality.
    '''
    def __init__(self, mydb):
        self.mydb = mydb
        self.is_logged_in = False

    def set_login(self, login):
        '''
        This method sets the login attribute to be the Tkinter login window.
        '''
        self.login = login 

    def collect_login(self): # collects data from login to existing account text fields
        '''
        This method is called when the "Confirm login" button is clicked.
        This method collects the data from the login to an existing account entries on the Login menu. 
        It then verifies that the user's username & password are correct.
        If the details are correct, it takes the user to the "Join an event" menu
        '''
        self.existing_username = self.login.get_existing_username()
        self.existing_password = self.login.get_existing_password()
        self.is_logged_in = login_code.validate_login(self.existing_username, self.existing_password, self.mydb)
        if self.is_logged_in == True:
            self.load_join_menu()
        elif self.is_logged_in == False:
            self.login.incorrect_password()
    
    def load_join_menu(self): # loads next menu if username matches password & withdraws current menu
        '''
        This method instantiates an object of class "JoinEventCommands".
        Next, it hides the login menu.
        It then collects the "join_event" window created by Tkinter, in "join_events_gui".
        Lastly, it sets this window to be an attribute of the object instantiated earlier in the method.
        '''
        joinEventCommand = JoinEventCommands(mydb, self.existing_username)
        self.login.login_window.withdraw()
        join_event = join_events_gui.join_events_menu(login.login_window, joinEventCommand.collect_join_event, joinEventCommand.collect_host_event)
        joinEventCommand.set_join_event(join_event)

    def collect_new_account(self): # collects data from new account text fields
        '''
        This method is called when the "Create account" button is clicked.
        It collects the username/password from their respective entries on the Login window
        Then, it validates & stores this information in the database by calling a function called "saved_to_db.
        '''
        username = self.login.get_new_username()
        password = self.login.get_new_password()
        saved_to_db = login_code.saving_new_account(username, password, self.mydb)
        if saved_to_db == True:
            self.login.made_new_account()
        elif saved_to_db == "Length":
            self.login.invalid_password_length()
        elif saved_to_db == "Character":
            self.login.invalid_password_character()
        elif saved_to_db == "Username":
            self.login.invalid_username_length()
        elif saved_to_db == "Exists":
            self.login.invalid_username_exists()


class JoinEventCommands: # encapsulates methods to collect & process data from join event menu
    '''
    This class encapsulates everything to do with the "Join Event" menu, such as its functionality & the window.
    '''
    def __init__(self, mydb, username):
        self.mydb = mydb
        self.username = username
    
    def set_join_event(self, join_event):
        '''
        This method sets the attribute "join_event" to be an object called "join_event".
        This object contains everything to do with the "Join event" window.
        '''
        self.join_event = join_event
        
    def collect_join_event(self): # collects data from join event code text field
        '''
        This method is called when the "Join Event" confirmation button is clicked.
        It collects the code that was inputted into the entry box.
        Then, it verifies if the id exists in the database.
        If the ID does exist, it checks if the user is already in the event by calling the function "check_username_in_event_members".
        If the ID exists, it takes the user to the visual calendar menu.
        '''
        self.eventID = self.join_event.get_join_event_code()
        id_exists = join_events_code.find_event_id(self.eventID, self.mydb)
        if id_exists:
            join_events_code.check_username_in_event_members(self.eventID, self.username, self.mydb)
            self.load_calendar_menu()
        else:
            self.join_event.invalid_code()
        
    def collect_host_event(self): # collects data from hosting event inputs
        '''
        This method is called when the "Host event" confirmation button is clicked.
        Firstly, it collects all of the inputs from the entry boxes & buttons on the page.
        Then, it generates a unique code for that event.
        Next, it validates the user's inputs against the criteria (e.g. correct format, length in range).
        If the event is valid, it displays the uniquely generated code to the user.
        '''
        selected_timeframe = self.join_event.get_timeframe_var()
        timeframe = join_events_code.find_timeframe(selected_timeframe)
        start_date = self.join_event.get_start_date()
        end_date = self.join_event.get_end_date()
        event_name = self.join_event.get_event_title()
        generated_code = join_events_code.generate_unique_code(self.mydb)
        valid_event = join_events_code.host_event(event_name, timeframe, start_date, end_date, generated_code, login.get_existing_username(), self.mydb)  
        if valid_event == True:
            self.join_event.display_unique_code(generated_code)
        elif valid_event == "Format":
            self.join_event.invalid_date_format()
        elif valid_event == "Logic":
            self.join_event.invalid_date_logic()
        elif valid_event == "Timeframe":
            self.join_event.invalid_date_timeframe()
        elif valid_event == "Title":
            self.join_event.invalid_title_length()

    def load_calendar_menu(self): # loads the calendar menu & hides join event menu
        '''
        This method loads the calendar menu.
        It first instantiates an object of the CalendarCommands class, then hides the "join event" window.
        Next, it collects an object containing all of the Tkinter widget information. 
        Then, it sets the eventID attribute, and the calendar_menu attribute.
        '''
        calendarCommand = CalendarCommands(self.mydb, self.username, self.eventID)
        self.join_event.join_events_window.withdraw()
        calendar_menu = calendar_gui.calendar_menu(login.login_window, calendarCommand.load_create_event_menu, calendarCommand.load_preferred_time_menu, calendarCommand.load_optimal_time_menu)
        calendar_menu.set_event_ID(self.eventID)
        calendarCommand.set_calendar_menu(calendar_menu)

class CalendarCommands:
    '''
    This class encapsulates all of the information to do with the calendar menu, such as its window & its functionality.
    '''
    def __init__(self, mydb, username, eventID):
        self.mydb = mydb
        self.username = username
        self.eventID = eventID

    def set_calendar_menu(self, calendar_menu):
        '''
        This method sets the attribute "calendar_menu" to contain the object that stores all information about the calendar window.
        '''
        self.calendar_menu = calendar_menu

    def load_create_event_menu(self): # loads create event menu & hides calendar menu
        '''
        This method is called when the "Add an event" button is clicked.
        It first instantiates an object of the "CreateEventCommands" class.
        Then, it hides the calendar menu. 
        Next, it collects an object that contains all the information about the "Create event" window from the "create_event_menu" function.
        Lastly, it sets this object as an attribute of the createEventCommand object.
        This causes the "Create an event" menu to appear on-screen.
        '''
        createEventCommand = CreateEventCommands(self.mydb, self.calendar_menu, self.username)
        self.calendar_menu.calendar_window.withdraw()
        create_event_menu = create_event_gui.create_event_menu(login.login_window, createEventCommand.create_event, createEventCommand.load_calendar_menu)
        createEventCommand.set_create_event_menu(create_event_menu)
    
    def load_preferred_time_menu(self): # loads preferred time menu, hides calendar window
        '''
        This method is called when the "Set preferred times" button is clicked.
        It firstly instantiates an object of the "SetPreferredTimeCommands" class.
        Then, it hides the calendar menu.
        Next, it collects an object from the "Set preferred times" menu which contains all the information about this window.
        It saves this object as the "set_preferred_time_menu" attribute of the "setPreferredTimeCommand" object.
        This causes the "Set preferred time" menu to appear on-screen.
        '''
        setPreferredTimeCommand = SetPreferredTimeCommands(self.mydb, self.calendar_menu, self.username)
        self.calendar_menu.calendar_window.withdraw()
        set_preferred_time_menu = set_preferred_time_gui.set_preferred_times_menu(login.login_window, setPreferredTimeCommand.set_preferred_time, setPreferredTimeCommand.load_calendar_menu)
        setPreferredTimeCommand.set_set_preferred_time_menu(set_preferred_time_menu)
    
    def load_optimal_time_menu(self): # loads optimal time menu, hides calendar window
        '''
        This method is called when the "View optimal times" button is clicked.
        It first instantiates an object of the "OptimalTimeCommands" class.
        Then, it hides the calendar window.
        Next, it collects a list of the best times by calling a function in the "calculate_optimal_time" module.
        It then collects an object from the function "optimal_time_menu" which contains information about the implementation of the GUI.
        Lastly, it sets this object as an attribute of the first object made in the function.
        This causes the "Choose Optimal Time" menu to appear on-screen.
        '''
        optimalTimeCommand = OptimalTimeCommands(self.mydb, self.calendar_menu)
        self.calendar_menu.calendar_window.withdraw()
        list_of_best_times = calculate_optimal_time.get_users_in_event(self.eventID, self.mydb)
        optimal_time_menu = optimal_time_gui.optimal_time_menu(login.login_window, optimalTimeCommand.load_calendar_menu, list_of_best_times)
        optimalTimeCommand.set_optimal_time_menu(optimal_time_menu)

class CreateEventCommands:
    def __init__(self, mydb, calendar_menu, username):
        self.mydb = mydb
        self.calendar_window = calendar_menu.calendar_window
        self.eventID = calendar_menu.eventID
        self.username = username
    
    def set_create_event_menu(self, create_event_menu):
        self.create_event_menu = create_event_menu
    
    def create_event(self):
        start_date = self.create_event_menu.get_start_date()
        end_date = self.create_event_menu.get_end_date()
        start_time = self.create_event_menu.get_start_time()
        end_time = self.create_event_menu.get_end_time()
        event_title = self.create_event_menu.get_event_title()
        is_repetitive = self.create_event_menu.get_is_repetitive()
        repetition_timeframe = self.create_event_menu.get_repetitive_timeframe()
        is_tentative = self.create_event_menu.get_is_tentative()
        new_event_created = create_event_code.create_event(start_date, end_date, join_events_code.validate_date_format, start_time, end_time, self.eventID, event_title, join_events_code.valid_title, is_repetitive, repetition_timeframe, is_tentative, self.username, mydb)
        if new_event_created == True:
            self.load_calendar_menu()
        # error message pop-up boxes
        elif new_event_created == "Date Format":
            self.create_event_menu.invalid_date_format()
        elif new_event_created == "Date Logic":
            self.create_event_menu.invalid_date_logic()
        elif new_event_created == "Timeframe":
            self.create_event_menu.invalid_date_timeframe()
        elif new_event_created == "Time Format":
            self.create_event_menu.invalid_time_format()
        elif new_event_created == "Time Logic":
            self.create_event_menu.invalid_time_logic()
        elif new_event_created == "Title":
            self.create_event_menu.invalid_title_length()
        elif new_event_created == "Repetition":
            self.create_event_menu.invalid_repetition()
        elif new_event_created == "Tentative":
            self.create_event_menu.invalid_tentability()

    def load_calendar_menu(self): # loads the calendar menu & hides join event menu
        self.create_event_menu.create_event_window.withdraw()
        self.calendar_window.deiconify()
    
class SetPreferredTimeCommands:
    def __init__(self, mydb, calendar_menu, username):
        self.mydb = mydb
        self.calendar_window = calendar_menu.calendar_window
        self.username = username
    
    def set_set_preferred_time_menu(self, set_preferred_time_menu):
        self.set_preferred_time_menu = set_preferred_time_menu
    
    def set_preferred_time(self):
        start_date = self.set_preferred_time_menu.get_start_date()
        end_date = self.set_preferred_time_menu.get_end_date()
        start_time = self.set_preferred_time_menu.get_start_time()
        end_time = self.set_preferred_time_menu.get_end_time()
        preferred_time_set = set_preferred_times_code.set_preferred_time(join_events_code.validate_date_format, start_date, end_date, create_event_code.valid_time_format, start_time, end_time, self.username, self.mydb)
        if preferred_time_set == True:
            self.load_calendar_menu()
        elif preferred_time_set == "Date Format":
            self.set_preferred_time_menu.invalid_date_format()
        elif preferred_time_set == "Date Logic":
            self.set_preferred_time_menu.invalid_date_logic()
        elif preferred_time_set == "Time Format":
            self.set_preferred_time_menu.invalid_time_format()
        elif preferred_time_set == "Time Logic":
            self.set_preferred_time_menu.invalid_time_logic()
        elif preferred_time_set == False:
            self.set_preferred_time_menu.error()

    def load_calendar_menu(self): 
        self.set_preferred_time_menu.set_preferred_time_window.withdraw()
        self.calendar_window.deiconify()

class OptimalTimeCommands:
    def __init__(self, mydb, calendar_menu):
        self.mydb = mydb
        self.calendar_window = calendar_menu.calendar_window
    
    def set_optimal_time_menu(self, optimal_time_menu):
        self.optimal_time_menu = optimal_time_menu
    
    def load_calendar_menu(self):
        self.optimal_time_menu.optimal_time_window.withdraw()
        self.calendar_window.deiconify()

if __name__ == '__main__':
    loginCommand = LoginCommands(mydb)
    login = login_gui.login_menu(loginCommand.collect_login, loginCommand.collect_new_account)
    loginCommand.set_login(login)

    # join_event.join_events_window.withdraw()
    login.login_window.mainloop()
