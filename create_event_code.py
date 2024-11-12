# create event code

import mysql.connector

from datetime import datetime

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
    print(host_start_date)
    return host_start_date 

def find_host_end_date(event_ID):# collects host end date from database
    mycursor = mydb.cursor()
    find_end_date_sql = "SELECT end_date FROM HOST_EVENTS WHERE eventID=%s"
    value = (event_ID, )
    mycursor.execute(find_end_date_sql, value)
    host_end_date = mycursor.fetchone()
    host_end_date = host_end_date[0].date()
    print(host_end_date)
    return host_end_date

def date_in_range(date, host_start_date, host_end_date): # finds if date is within host range
    return host_start_date <= date <= host_end_date

def convert_date_format(date):
    return datetime.strptime(date, '%d/%m/%y').date()

def validate_dates(start_date, end_date, valid_date_format, eventID): # checks if dates are valid
    is_valid_start_date = valid_date_format(start_date)
    is_valid_end_date = valid_date_format(end_date)
    host_start_date = find_host_start_date(eventID)
    host_end_date = find_host_end_date(eventID)
    if is_valid_start_date and is_valid_end_date:
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        start_before_end = start_date_before_end_date(start_date, end_date)
        if start_before_end:
            start_date_in_range = date_in_range(start_date, host_start_date, host_end_date)
            end_date_in_range = date_in_range(end_date, host_start_date, host_end_date)
            if start_date_in_range and end_date_in_range:
                print("Both dates in range")
                return True
            else:
                print("One of the dates not in range")      
                return False  
        else:
            print("Start date after end date")
            return False
    else:
        print("Invalid date format")
        return False

def valid_time_format(time):
    try :
        time = datetime.strptime(time, '%H:%M')
    except:
        return False
    else:
        return True

def start_time_before_end_time(start_time, end_time):
    return start_time <= end_time

def validate_time(start_time, end_time, start_date, end_date):
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
                return False
        else:
            print("Times valid")
            return True
    else:
        print("Invalid times")
        return False
    
def convert_repetition(is_repetitive):
    if is_repetitive == 1:
        return "Yes"
    elif is_repetitive == 2:
        return "No"
    else:
        return False

def convert_repetition_timeframe(is_repetitive, repetition_timeframe):
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

def convert_is_tentative(is_tentative):
    if is_tentative == 1:
        return "Yes"
    elif is_tentative == 2:
        return "No"
    else:
        return False
    
class userEvent:
    def __init__(eventID, event_title, )

def store_event_to_database(start_date, end_date, start_time, end_time, eventID, event_title, is_repetitive, repetition_timeframe, is_tentative, username):
    mycursor = mydb.cursor()
    

    
def create_event(start_date, end_date, valid_date_format, start_time, end_time, eventID, event_title, valid_title, is_repetitive, repetition_timeframe, is_tentative, username): # creates event in database
    dates_valid = validate_dates(start_date, end_date, valid_date_format, eventID)
    title_valid = valid_title(event_title)
    is_repetitive = convert_repetition(is_repetitive)
    repetition_timeframe = convert_repetition_timeframe(is_repetitive, repetition_timeframe)
    print(is_repetitive, repetition_timeframe)
    is_tentative = convert_is_tentative(is_tentative)
    print(is_tentative)
    if dates_valid:
        start_date = convert_date_format(start_date)
        end_date = convert_date_format(end_date)
        times_valid = validate_time(start_time, end_time, start_date, end_date)


