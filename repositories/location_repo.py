from db.run_sql import run_sql
from models.location import Location

# helper funcs
def make_location(row):
    return Location(row['name'], row['capacity'], row['id'])

#create
def save(location):
    sql = "INSERT INTO locations (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [location.room_name, location.capacity]
    result = run_sql(sql, values)
    location.id = result[0]['id']
    return location

#read
def select(id):
    location = None
    result = run_sql("SELECT * FROM locations WHERE id = %s", [id])

    if result is not None:
        location = make_location(result[0])
    return location

def select_all():
    results = run_sql("SELECT * FROM locations")
    return [make_location(row) for row in results]

#update

#delete
def delete_all():
    run_sql("DELETE FROM locations")

def delete(id):
    run_sql("DELETE FROM locations WHERE id = %s", [id])