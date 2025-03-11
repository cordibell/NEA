# create event code

import mysql.connector
from datetime import datetime

# datebase connection

mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

def start_date_before_end_date(start_date, end_date): # finds if start date is before end date
    return start_date <= end_date

def find_host_start_date(event_ID): # collects host start date from database
    mycursor = mydb.cursor()
    find_start_date_sql = "SELECT start_date FROM HOST_EVENTS WHERE eventID=%s"
    value = (event_ID, )
    mycursor.execute(find_start_date_sql, value)
    host_start_date = mycursor.fetchone()
    host_start_date = host_start_date[0].date()
    return host_start_date 

def find_host_end_date(event_ID):# collects host end date from database
    mycursor = mydb.cursor()
    find_end_date_sql = "SELECT end_date FROM HOST_EVENTS WHERE eventID=%s"
    value = (event_ID, )
    mycursor.execute(find_end_date_sql, value)
    host_end_date = mycursor.fetchone()
    host_end_date = host_end_date[0].date()
    return host_end_date

def date_in_range(date, host_start_date, host_end_date): # finds if date is within host range
    return host_start_date <= date <= host_end_date

def convert_date_format(date): # converts date from string to datetime object
    return datetime.strptime(date, '%d/%m/%y').date()

def validate_dates(start_date, end_date, valid_date_format, eventID): # checks if dates are valid format (DD/MM/YY) & logical
    is_valid_start_date = valid_date_format(start_date)
    is_valid_end_date = valid_date_format(end_date)
    # collects host start/end date
    host_start_date = find_host_start_date(eventID)
    host_end_date = find_host_end_date(eventID)
    if is_valid_start_date and is_valid_end_date: # if start/end dates are valid
        # converts start/end date into datetime object
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        start_before_end = start_date_before_end_date(start_date, end_date) # checks if start date is before end date
        if start_before_end: # if start is before end, checks dates are in host event ranges
            start_date_in_range = date_in_range(start_date, host_start_date, host_end_date)
            end_date_in_range = date_in_range(end_date, host_start_date, host_end_date)
            if start_date_in_range and end_date_in_range:
                return True # both dates in range
            else:
                return "Timeframe" # dates not in timeframe range
        else:
            return "Date Logic" # start date after end date
    else:
        return "Date Format" # invalid date format

def valid_time_format(time): # validates the time format HH:MM
    try :
        time = datetime.strptime(time, '%H:%M')
    except:
        return False
    else:
        return True

def start_time_before_end_time(start_time, end_time): # checks if start time is before end time
    return start_time <= end_time

def validate_time(start_time, end_time, start_date, end_date): # validates if times are in correct format
    valid_start_time = valid_time_format(start_time)
    valid_end_time = valid_time_format(end_time)
    if valid_end_time and valid_start_time: # both times are valid format
        # converts times to datetime objects
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = datetime.strptime(end_time, '%H:%M').time()
        if start_date == end_date: # if date is same
            start_before_end_time = start_time_before_end_time(start_time, end_time) # checks the start time is before end time
            if start_before_end_time: # valid time (same day)
                return True
            else:
                return "Time Logic" # invalid time (same day)
        else:
            return True # valid time (not same day)
    else:
        return "Time Format" # incorrect format
    
def convert_repetition(is_repetitive): # converts repetition IntVars to strings for database storage
    if is_repetitive == 1:
        return "Yes"
    elif is_repetitive == 2:
        return "No"
    else:
        return False

def convert_repetition_timeframe(is_repetitive, repetition_timeframe): # converts repetition timeframe IntVars to strings
    if is_repetitive == "No":
        return "N/A"
    elif is_repetitive == False:
        return False
    elif repetition_timeframe == 1:
        return "Daily"
    elif repetition_timeframe == 2:
        return "Weekly"
    elif repetition_timeframe == 3:
        return "Monthly"
    elif repetition_timeframe == 4:
        return "Custom"
    else:
        return False

def convert_is_tentative(is_tentative): # converts tentative IntVars to strings for database storage
    if is_tentative == 1:
        return "Yes"
    elif is_tentative == 2:
        return "No"
    else:
        return False
    
class userEvent:
    '''
    This class contains the attributes of a new user-created event
    '''
    def __init__(self, event_title, event_start, event_end, is_repetitive, repetition_timeframe, is_tentative, username):
        self.event_title = event_title
        self.event_start = event_start
        self.event_end = event_end
        self.is_repetitive = is_repetitive
        self.repetition_timeframe = repetition_timeframe
        self.is_tentative = is_tentative
        self.username = username

    def store_event_to_database(self, mydb): # stores event to database entity "USER_EVENTS"
        mycursor = mydb.cursor()
        save_event_sql = "INSERT INTO USER_EVENTS (name, username, event_start, event_end, is_repetitive, repetition_timeframe, is_tentative) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.event_title, self.username, self.event_start, self.event_end, self.is_repetitive, self.repetition_timeframe, self.is_tentative)
        mycursor.execute(save_event_sql, values)
        mydb.commit()
        return True
    

    
def create_event(start_date, end_date, valid_date_format, start_time, end_time, eventID, event_title, valid_title, is_repetitive, repetition_timeframe, is_tentative, username, mydb): # creates event in database
    # this function validates the inputs & if they're valid stores them in the database
    dates_valid = validate_dates(start_date, end_date, valid_date_format, eventID) # checks if dates are valid
    if dates_valid == "Date Format": # if dates are invalid format
        return "Date Format"
    elif dates_valid == "Date Logic": # if start date after end date
        return "Date Logic"
    elif dates_valid == "Timeframe": # user dates don't match host event date range
        return "Timeframe"
    title_valid = valid_title(event_title)
    if not title_valid: # title is invalid
        return "Title"
    is_repetitive = convert_repetition(is_repetitive)
    if not is_repetitive: # no repetition option selected
        return "Repetition"
    repetition_timeframe = convert_repetition_timeframe(is_repetitive, repetition_timeframe)
    if not repetition_timeframe: # user hasn't selected an appropriate repetition timeframe length
        return "Repetition"
    is_tentative = convert_is_tentative(is_tentative)
    if not is_tentative: # user hasn't selected a tentative option
        return "Tentative"
    # converts start/end date format to datetime objects
    start_date = convert_date_format(start_date)
    end_date = convert_date_format(end_date)
    times_valid = validate_time(start_time, end_time, start_date, end_date) # validates time format/logic
    if times_valid == "Time Format": # invalid time format (not HH:MM)
        return "Time Format"
    elif times_valid == "Time Logic": # start time after end time & date is same
        return "Time Logic"
    # converts times into a datetime object
    start_time = datetime.strptime(start_time, '%H:%M').time()
    end_time = datetime.strptime(end_time, '%H:%M').time()
    # combines start date/time & end date/time into one datetime object
    event_start = datetime.combine(start_date, start_time)
    event_end = datetime.combine(end_date, end_time)
    # instantiates new object of userEvent class.
    new_event = userEvent(event_title, event_start, event_end, is_repetitive, repetition_timeframe, is_tentative, username)
    saved_to_database = new_event.store_event_to_database(mydb) # saves event to database
    if saved_to_database:
        return True


