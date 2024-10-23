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
    return start_date < end_date

def find_host_start_date(event_ID): # collects host start date from database
    mycursor = mydb.cursor()
    find_start_date_sql = "SELECT start_date FROM HOST_EVENTS WHERE eventID=%s"
    value = (event_ID, )
    mycursor.execute(find_start_date_sql, value)
    host_start_date = mycursor.fetchone()
    host_start_date = datetime.strptime(host_start_date, '%Y-%m-%d %H:%M:%S').date()
    return host_start_date 

def find_host_end_date(event_ID):# collects host end date from database
    mycursor = mydb.cursor()
    find_end_date_sql = "SELECT end_date FROM HOST_EVENTS WHERE eventID=%s"
    value = (event_ID, )
    mycursor.execute(find_end_date_sql, value)
    host_end_date = mycursor.fetchone()
    host_end_date = datetime.strptime(host_end_date, '%Y-%m-%d %H:%M:%S').date()
    return host_end_date

def date_in_range(date, host_start_date, host_end_date): # finds if date is within host range
    return host_start_date <= date <= host_end_date

    
def create_event(start_date, end_date, valid_date_format, eventID): # creates event in database
    is_valid_start_date = valid_date_format(start_date)
    is_valid_end_date = valid_date_format(end_date)
    host_start_date = find_host_start_date(eventID)
    host_end_date = find_host_end_date(eventID)
    if is_valid_start_date and is_valid_end_date:
        start_date = datetime.strptime(start_date, '%d/%m/%y').date()
        end_date = datetime.strptime(end_date, '%d/%m/%y').date()
        start_before_end = start_date_before_end_date(start_date, end_date)
        if start_before_end:
            start_date_in_range = date_in_range(start_date, host_start_date, host_end_date)
            end_date_in_range = date_in_range(end_date, host_start_date, host_end_date)
            if start_date_in_range and end_date_in_range:
                print("Both dates in range")
            else:
                print("One of the dates not in range")        
        else:
            print("Start date after end date")
    else:
        print("Invalid date format")
