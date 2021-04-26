from db.run_sql import run_sql
from models.member import Member

# helper func
def make_member(row):
    return Member(row['first_name'], row['last_name'], row['premium'], row['active'], row['id'])

# create
def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium, member.active]
    result = run_sql(sql, values)
    member.id = result[0]["id"]
    return member

# read
def select(id):
    member = None
    result = run_sql("SELECT * FROM members WHERE id = %s", [id])
    
    if result is not None:
        member = make_member(result)
    return member

def select_all():
    results = run_sql("SELECT * FROM members")
    return [make_member(row) for row in results]

# update

# delete
def delete_all():
    run_sql("DELETE FROM members")

def delete(id):
    run_sql("DELETE FROM members WHERE id = %s", [id])