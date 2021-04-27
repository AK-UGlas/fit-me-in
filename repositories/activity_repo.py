from db.run_sql import run_sql
from datetime import datetime, time, timedelta
from dateutil.parser import isoparse
from models.booking import Booking
from models.location import Location

import repositories.location_repo as loc_repo

# helper functions
def make_activity(row):
    name = row['activity_name']
    location = loc_repo.select(row['location_id'])
    start = isoparse(row['start_time'])

    return Activity(name, start, location, row['id'])

#create
def save(activity):
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

# update

# delete
def delete_all():
    run_sql("DELETE FROM activities")

def delete(id):
    run_sql("DELETE FROM activities WHERE id = %s", [id])
