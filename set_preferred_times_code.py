# set preferred times code menu, made 10/12/24

import mysql.connector
from datetime import datetime

# Connecting to database

mydb = mysql.connector.connect(
    host="10.0.2.214",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

def start_date_before_end_date(start_date, end_date): # finds if start date is before end date
    return start_date <= end_date

def convert_date_format(date): # converts date format from string to datetime object
    return datetime.strptime(date, '%d/%m/%y').date()

def validate_dates(valid_date_format, start_date, end_date): # checks if dates are valid
    start_date_valid = valid_date_format(start_date)
    end_date_valid = valid_date_format(end_date)
    if start_date_valid and end_date_valid: # both dates valid format
        # converts dates from string to datetime objects
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        start_before_end = start_date_before_end_date(start_date, end_date) # checks if start date is before end date
        if start_before_end:
            return True # dates valid
        else:
            return "Date Logic" # start date after end date
    else:
        return "Date Format" # invalid date format
    
def start_time_before_end_time(start_time, end_time): # checks if start time is before end time
    return start_time <= end_time
    
def validate_time(valid_time_format, start_time, end_time, start_date, end_date): # validates times format/logic
    valid_start_time = valid_time_format(start_time)
    valid_end_time = valid_time_format(end_time)
    if valid_end_time and valid_start_time: # if both times valid format
        # converts into datetime objects
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = datetime.strptime(end_time, '%H:%M').time()
        if start_date == end_date: # if same day
            start_before_end_time = start_time_before_end_time(start_time, end_time) # checks start time is before end time
            if start_before_end_time:
                return True # times valid (same day)
            else:
                return "Time Logic" # times invalid (same day)
        else:
            return True # times valid (different day)
    else:
        return "Time Format" # invalid time format

def set_preferred_time(valid_date_format, start_date, end_date, valid_time_format, start_time, end_time, username, mydb):
     # called when confirmation button pressed, validates inputs & saves to database
    dates_valid = validate_dates(valid_date_format, start_date, end_date) # validates dates
    if dates_valid != "Date Format" and dates_valid != "Date Logic": # if dates are valid
        # converts from strings to datetime objects
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        times_valid = validate_time(valid_time_format, start_time, end_time, start_date, end_date) # checks if times are valid
        if times_valid != "Time Format" and times_valid != "Time Logic": # if times are valid
            # converts times from strings to datetime objects
            start_time = datetime.strptime(start_time, '%H:%M').time()
            end_time = datetime.strptime(end_time, '%H:%M').time()
            # combines dates/times into one datetime object
            preferred_start = datetime.combine(start_date, start_time)
            preferred_end = datetime.combine(end_date, end_time)
            saved_to_database = save_to_database(preferred_start, preferred_end, username, mydb) # saves to database
            if saved_to_database:
                return True
            else:
                return False
        else:
            return times_valid # invalid time format/logic
    else:
        return dates_valid # invalid date format/logic

def save_to_database(preferred_start, preferred_end, username, mydb): # saves preferred start & end time to database
    mycursor = mydb.cursor()
    save_time_sql = "UPDATE USERS SET preferred_time_start=%s, preferred_time_end=%s WHERE username=%s"
    values = (preferred_start, preferred_end, username)
    mycursor.execute(save_time_sql, values)
    mydb.commit()
    return True

    
