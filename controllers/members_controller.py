from datetime import datetime
from flask import Flask, Blueprint, redirect, render_template, request, url_for

from models.member import Member
import repositories.member_repo as member_repo

members_bp = Blueprint("members", __name__)

# new member form
@members_bp.route("/members/join")
def new_member():
    return render_template("members/join.html", title="become a member")

# add new member and display dashboards
@members_bp.route("/members/join")
def create_member():
    first = request.form['first-name']
    last = request.form['last-name']
    email = request.form['email']
    premium = request.form['premium']
    
    new_member = member_repo.save( Member(first, last, email, premium) ) 

    return redirect(url_for('.welcome_dashboard', id=new_member.id))

# verify member exists in database. if not render error page
# prompting user to create account
@members_bp.route("/members/verify", methods=["GET", "POST"])
def check_member_email():
    member = member_repo.select_for_email(request.form['email'])

    if member is not None:
        return redirect(url_for('.welcome_dashboard', id=member.id))
    
    return render_template("/members/error.html", title="Error: member not found")

@members_bp.route("/members/dash_<id>")
def welcome_dashboard(id):
    member = member_repo.select(id)
    # get the current time - we'll use this to
    # determine which classes are upcoming
    current_time = datetime.today()

    return render_template('members/dashboard.html', member=member)