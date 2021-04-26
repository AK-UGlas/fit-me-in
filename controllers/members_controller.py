from flask import Flask, Blueprint, redirect, render_template

from models.member import Member
import repositories.member_repo as member_repo

members_bp = Blueprint("members", __name__)

# join
@members_bp.rout("members/join")
def new_member():
    pass

# index
@members_bp.route("/members/<id>")
def member_dashboard(id):
    member = member_repo.select(id)
    return render_template('members/dashboard.html', member=member)