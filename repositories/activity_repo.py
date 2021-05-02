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

def upcoming(date_obj):
    date = date_obj.date().isoformat()
    time = date_obj.time().isoformat() 
    return select_by_date(date, time)

# ensure chosen activity doesn't conflict with other classes
def timeslot_available(activity):
    date = activity.start.date()
    time = activity.start.time()
    loc = activity.location.id
    
    sql = "SELECT * FROM activities WHERE date = %s AND location_id = %s"
    values = [date, loc]
    results = run_sql(sql, values)
    
    # if no hits, return 
    if not results: 
        return False

    dt_obj = datetime.combine(date, time)
    for row in results:
        # ignore activity with same id (when updating)
        if activity.id == row['id']:
            continue
        conflict_time = datetime.combine(date, row['start_time'])
        delta = dt_obj - conflict_time
        if delta.seconds > 82800 or delta.seconds < 3600:
            return True
    
    return False

#create
def save(activity):
    clash = timeslot_available(activity)
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

    if result:
        activity = make_activity(result[0])
    return activity

def select_by_date(date, time):
    sql = "SELECT * FROM activities WHERE date = %s AND start_time > %s ORDER BY start_time ASC"
    values = [date, time]
    results = run_sql(sql, values)
    
    return [make_activity(row) for row in results]

# update
def update(activity):
    # check the update won't conflict with existing activities
    clash = timeslot_available(activity)
    if clash:
        print("conflict detected")
        return False

    sql = "UPDATE activities SET (activity_name, start_time, date, location_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [activity.name, activity.get_start_time(True), activity.get_date(True), activity.location.id, activity.id]
    run_sql(sql, values)

    return True

# delete
def delete_all():
    run_sql("DELETE FROM activities")

def delete(id):
    run_sql("DELETE FROM activities WHERE id = %s", [id])
