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

def convert_date_format(date):
    return datetime.strptime(date, '%d/%m/%y').date()

def validate_dates(valid_date_format, start_date, end_date): # checks if dates are valid
    start_date_valid = valid_date_format(start_date)
    end_date_valid = valid_date_format(end_date)
    if start_date_valid and end_date_valid:
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        start_before_end = start_date_before_end_date(start_date, end_date)
        if start_before_end:
            print("Both dates valid")
            return True
        else:
            print("End date before start")
            return "Date Logic"
    else:
        print("Invalid date format")
        return "Date Format"
    
def start_time_before_end_time(start_time, end_time):
    return start_time <= end_time
    
def validate_time(valid_time_format, start_time, end_time, start_date, end_date): # validates times
    valid_start_time = valid_time_format(start_time)
    valid_end_time = valid_time_format(end_time)
    if valid_end_time and valid_start_time:
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = datetime.strptime(end_time, '%H:%M').time()
        if start_date == end_date:
            start_before_end_time = start_time_before_end_time(start_time, end_time)
            if start_before_end_time:
                print("Both times valid")
                return True
            else:
                print("Start time after end time")
                return "Time Logic"
        else:
            print("Times valid")
            return True
    else:
        print("Invalid times")
        return "Time Format"

def set_preferred_time(valid_date_format, start_date, end_date, valid_time_format, start_time, end_time, username, mydb): # called when confirmation button pressed
    dates_valid = validate_dates(valid_date_format, start_date, end_date)
    if dates_valid != "Date Format" and dates_valid != "Date Logic":
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        times_valid = validate_time(valid_time_format, start_time, end_time, start_date, end_date)
        if times_valid != "Time Format" and times_valid != "Time Logic":
            start_time = datetime.strptime(start_time, '%H:%M').time()
            end_time = datetime.strptime(end_time, '%H:%M').time()
            preferred_start = datetime.combine(start_date, start_time)
            preferred_end = datetime.combine(end_date, end_time)
            print(f"Preferred start: {preferred_start}\nPreferred end: {preferred_end}")
            saved_to_database = save_to_database(preferred_start, preferred_end, username, mydb)
            if saved_to_database:
                return True
            else:
                return False
        else:
            return times_valid
    else:
        return dates_valid

def save_to_database(preferred_start, preferred_end, username, mydb): # saves preferred start & end time to database
    mycursor = mydb.cursor()
    save_time_sql = "UPDATE USERS SET preferred_time_start=%s, preferred_time_end=%s WHERE username=%s"
    values = (preferred_start, preferred_end, username)
    mycursor.execute(save_time_sql, values)
    mydb.commit()
    print(f"Saved preferred time to database")
    return True

    
