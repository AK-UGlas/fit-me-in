from db.run_sql import run_sql
from models.member import Member
from models.booking import Booking
from models.activity import Activity

import repositories.activity_repo as act_repo
import repositories.member_repo as member_repo

# helper functions
def make_booking(row):
    member = member_repo.select(row['member_id'])
    activity = act_repo.select(row['activity_id'])
    return Booking(member, activity)

# create
def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking

# read
def select_all():
    results = run_sql("SELECT * FROM bookings")
    return [make_booking(row) for row in results]

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    return make_booking(result)

def select_members_of_activity(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        member = member_repo.make_member(row)
        members.append(member)

    return members

def select_activities_of_member(id):
    activities = []
    sql = "SELECT activities.* FROM activities INNER JOIN bookings ON bookings.activity_id = activities.id WHERE bookings.member_id = %s ORDER BY activities.date, activities.start_time"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        activity = act_repo.make_activity(row)
        activities.append(activity)

    return activities
    
        