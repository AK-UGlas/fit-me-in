from db.run_sql import run_sql
from models.location import Location

#create
def save(location):
    sql = "INSERT INTO locations (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [location.room_name, location.capacity]
    result = run_sql(sql, values)
    location.id = result[0]['id']
    return location

#read

#update

#delete