import pdb
from db.run_sql import run_sql
from models.member import Member

# helper func
def make_member(row):
    return Member(row['first_name'], row['last_name'], row['email'], row['premium'], row['active'], row['id'])

# create
def save(member):
    sql = "INSERT INTO members (first_name, last_name, email, premium, active) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.email, member.premium, member.active]
    result = run_sql(sql, values)
    member.id = result[0]["id"]
    return member

# read
def select(id):
    member = None
    result = run_sql("SELECT * FROM members WHERE id = %s", [id])
    
    if result:
        member = make_member(result[0])
    return member

def select_for_email(email):
    member = None
    result = run_sql("SELECT * FROM members WHERE email = %s", [email])
    #pdb.set_trace()
    if result:
        member = make_member(result[0])
    return member

def select_all():
    results = run_sql("SELECT * FROM members")
    return [make_member(row) for row in results]

# update
def update(member):
    sql = "UPDATE members SET (first_name, last_name, email, premium, active) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.email, member.premium, member.active]
    run_sql(sql, values)

# delete
def delete_all():
    run_sql("DELETE FROM members")

def delete(id):
    run_sql("DELETE FROM members WHERE id = %s", [id])