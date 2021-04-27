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