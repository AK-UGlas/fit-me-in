import pdb
from db.run_sql import run_sql
from datetime import datetime, time, timedelta
from dateutil.parser import isoparse
from models.booking import Booking
from models.location import Location
from models.activity import Activity

import repositories.location_repo as loc_repo

# helper functions
def make_activity(row):
    name = row['activity_name']
    location = loc_repo.select(row['location_id'])
    start = datetime.combine(row['date'], row['start_time'])

    return Activity(name, start, location, row['id'])

# ensure chosen activity doesn't conflict with other classes
def timeslot_available(date, time, loc):
    sql = "SELECT * FROM activities WHERE date = %s AND location_id = %s"
    values = [date, loc]
    results = run_sql(sql, values)
    
    # if no hits, return 
    if not results: 
        return False

    dt_obj = datetime.combine(date, time)
    for row in results:
        conflict_time = datetime.combine(date, row['start_time'])
        delta = dt_obj - conflict_time
        if delta.seconds > 82800 or delta.seconds < 3600:
            return True
    
    return False

#create
def save(activity):
    clash = timeslot_available(activity.start.date(), activity.start.time(), activity.location.id)
    if clash:
        print("conflict detected")
        return None
    sql = "INSERT INTO activities(activity_name, start_time, date, location_id) VALUES (%s, %s, %s, %s) RETURNING id"

    # set date and time formats as ISO 8601 strings
    start = activity.start.time().isoformat()
    date = activity.start.date().isoformat()

    values = [activity.name, start, date, activity.location.id]
    result = run_sql(sql, values)

    activity.id = result[0]['id']
    return activity

# read
def select(id):
    activity = None
    result = run_sql("SELECT * FROM activities WHERE id = %s", [id])

    if result is not None:
        activity = make_activity(result[0])
    return activity

def select_by_date(date, time):
    sql = "SELECT * FROM activities WHERE date = %s AND start_time > %s"
    values = [date, time]
    results = run_sql(sql, values)
    
    return [make_activity(row) for row in results]

# update

# delete
def delete_all():
    run_sql("DELETE FROM activities")

def delete(id):
    run_sql("DELETE FROM activities WHERE id = %s", [id])
