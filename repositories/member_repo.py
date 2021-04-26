from db.run_sql import run_sql
from models.member import Member

# create
def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium, member.active]
    result = run_sql(sql, values)
    member.id = result[0]["id"]
    return member

# read


# update

# delete
def delete_all():
    run_sql("DELETE FROM members")

def delete(id):
    run_sql("DELETE FROM members WHERE id = %s", [id])