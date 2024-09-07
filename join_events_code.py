# join_events code, made 29/09/24

import mysql.connector
from datetime import datetime
import calendar

# Connecting to database
mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

def find_timeframe(selected_timeframe):
    if selected_timeframe == 1:
        timeframe = "1 day"
    elif selected_timeframe == 2:
        timeframe = "1 week"
    elif selected_timeframe == 3:
        timeframe = "1 month"
    elif selected_timeframe == 4:
        timeframe = "3 months"
    else:
        timeframe="Error"
    return timeframe

def validate_dates(start_date, end_date, timeframe): # Checks if the dates are valid in the given timeframe
    valid_start_date = validate_date_format(start_date)
    valid_end_date = validate_date_format(end_date)
    if valid_start_date and valid_end_date:
        start_date = datetime.strptime(start_date, '%d/%m/%y').date()
        end_date = datetime.strptime(end_date, '%d/%m/%y').date()
        valid_length = validate_timeframe_length(start_date, end_date, timeframe)
        if valid_length:
            return True
    else:
        return False


def validate_date_format(date): # checks if the dates are in the correct format
    try:
        valid_date = datetime.strptime(date, '%d/%m/%y').date()
    except:
        return False
    else:
        return True

def validate_timeframe_length(start_date, end_date, timeframe): # checks if dates are within given timeframe
    length = find_number_of_days(start_date, end_date)
    timeframe = convert_timeframe(start_date, end_date, timeframe)
    # checking if dates are within timeframe
    if length < 0:
        print("End date before start date")
        return False
    elif length > timeframe:
        print("Timeframe too short")
        return False
    elif length < timeframe:
        print("Timeframe too long")
        return False
    else:
        print("Valid timeframe!")
        return True
    
def convert_timeframe(start_date, end_date, timeframe): # converts timeframes to integers
    if timeframe == "1 day":
        timeframe = 1
    elif timeframe == "1 week":
        timeframe = 7
    elif timeframe == "1 month":
        timeframe = calendar._monthlen(start_date.year, start_date.month)
    elif timeframe == "3 months":
        timeframe = 0
        month = start_date.month
        year = start_date.year
        for i in range(3):
            if month <= 11: # year wont overlap
                timeframe += calendar._monthlen(year, month)
                month += 1
            elif month == 12:
                timeframe += calendar._monthlen(year, 1)
                year += 1
                month = 1
    return timeframe

def valid_title(event_name): # validates if title is between 1-128 characters
    print(f"Length of string: {len(event_name)}")
    if len(event_name) > 128 or len(event_name) < 1:
        print("Invalid title")
        return False
    else:
        print("Valid title")
        return True

def find_number_of_days(start_date, end_date): # finds number of days between two dates
    length = end_date-start_date
    print(f"Distance between dates: {length.days}")
    return length.days

def host_event(event_name, timeframe, start_date, end_date): # creates an object for an event & saves it to database
    is_valid_dates = validate_dates(start_date, end_date, timeframe)
    is_valid_title = valid_title(event_name)
    if is_valid_dates and is_valid_title:
        start_date = datetime.strptime(start_date, '%d/%m/%y').date()
        end_date = datetime.strptime(end_date, '%d/%m/%y').date()
        new_event = Host_event(event_name, timeframe, start_date, end_date)
        new_event.save_event_info(mydb)
    else:
        print("Can't save to database")

class Host_event: # event hosted by a user, where they are trying to find out availability for it
    def __init__(self, event_name, timeframe, start_date, end_date):
        self.event_name = event_name
        self.timeframe = timeframe
        self.start_date = start_date
        self.end_date = end_date

    def save_event_info(self, mydb):
        print("Saved event info to database")
