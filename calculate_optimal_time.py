# calculate optimal time file, created 11/12/24

import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

class userEvent:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

class timeSlot: # each hour timeslot that the event could possibly be in
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.score = 0
    
    def increase_score(self):
        self.score += 1

def get_users_in_event(eventID, mydb): # collects all the users who are part of an event from EVENT_MEMBERS TABLE
    mycursor = mydb.cursor()
    find_users_sql = "SELECT username FROM EVENT_MEMBERS WHERE eventID = %s"
    values = (eventID, )
    mycursor.execute(find_users_sql, values)
    users_in_event = mycursor.fetchall() 
    list_of_users_in_event = []   
    print(users_in_event)
    for user in users_in_event:
        list_of_users_in_event.append(user[0])
    print(list_of_users_in_event)
    list_of_event_objects = find_events_from_user_in_database(list_of_users_in_event, mydb)
    list_of_timeslots = find_timeslots_range(eventID, mydb)
    calculate_timeslot_score(list_of_timeslots, list_of_event_objects)

def find_events_from_user_in_database(list_of_users_in_event, mydb): # finds all events in USER_EVENTS table for each user
    mycursor = mydb.cursor()
    list_of_events_found = []
    for user in list_of_users_in_event:
        find_event_sql = "SELECT userEventID, event_start, event_end FROM USER_EVENTS WHERE username = %s"
        values = (user, )
        mycursor.execute(find_event_sql, values)
        event_found = mycursor.fetchall()
        list(event_found)
        list_of_events_found.append(event_found)
    print(list_of_events_found)
    list_of_event_objects = convert_events_into_objects(list_of_events_found)
    return list_of_event_objects

def convert_events_into_objects(list_of_events_found): # converts the items in the list into a list of objects of class userEvents
    list_of_event_objects = []
    for users_events in list_of_events_found:
        for event in users_events:
            event_id = event[0]
            start = event[1]
            end = event[2]
            list_of_event_objects.append(userEvent(event_id, start, end))
    for event in list_of_event_objects:
        print(event.start, event.end)
    return list_of_event_objects

def find_timeslots_range(eventID, mydb): # finds start date & end date of host event from database-
    mycursor = mydb.cursor()
    find_timeslot_sql = "SELECT start_date, end_date FROM HOST_EVENTS WHERE eventID = %s"
    values = (eventID,)
    mycursor.execute(find_timeslot_sql, values)
    myresult = mycursor.fetchone()
    start_date = myresult[0]
    end_date = myresult[1]
    print(start_date)
    print(end_date)
    list_of_timeslots = create_timeslots(start_date, end_date)
    return list_of_timeslots
    
def create_timeslots(start_date, end_date): # creates timeslot objects for each timeslot in the range
    list_of_timeslots = []
    current_date = start_date
    while current_date <= end_date:
        hour = 8
        current_time = datetime.time(hour, 0, 0)
        while hour <= 22:
            timeslot_start = datetime.datetime.combine(current_date, current_time)
            hour += 1
            current_time = datetime.time(hour, 0, 0)
            timeslot_end = datetime.datetime.combine(current_date, current_time)
            list_of_timeslots.append(timeSlot(timeslot_start, timeslot_end))
        current_date += datetime.timedelta(days=1)
    print(list_of_timeslots)
    print(type(list_of_timeslots))
    return list_of_timeslots

def calculate_timeslot_score(list_of_timeslots, list_of_event_objects):
    for timeslot in list_of_timeslots:
        for event in list_of_event_objects:
            if event.end >= timeslot.start and event.start <= timeslot.end:
                timeslot.increase_score()
        print(f"Start: {timeslot.start}. End: {timeslot.end}. Score: {timeslot.score}")


get_users_in_event("39G09DN8", mydb)
