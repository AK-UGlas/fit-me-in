from datetime import datetime
from flask import Flask, Blueprint, redirect, render_template, request, url_for

from models.member import Member
import repositories.member_repo as member_repo
import repositories.activity_repo as act_repo

members_bp = Blueprint("members", __name__)

# helper function - generate a new member from form data
def generate_member(form):
    first = form['first-name']
    last = form['last-name']
    email = form['email']
    premium = False
    if premium in form:
        premium = True
    return Member(first, last, email, premium)

# new member form
@members_bp.route("/members/join")
def new_member():
    return render_template("members/join.html", title="become a member")

# add new member and display dashboards
@members_bp.route("/members/join", methods=['POST'])
def create_member(): 
    member = member_repo.save( generate_member(request.form) ) 
    return redirect(url_for('.welcome_dashboard', id=member.id))

# edit user details
@members_bp.route("/members/<id>/edit")
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member=member)

# update details and return to dashboard
@members_bp.route("/members/<id>/update", methods=['POST'])
def update_member(id):
    # create member object from form info
    member = generate_member(request.form)
    member.id = id
    if active not in request.form:
        member.active = False
    return render_template('members/dashboard.html', member=member)
    

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
    dt = datetime.today().replace(second=0, microsecond=0)
    upcoming = act_repo.select_by_date( dt.date().isoformat(), dt.time().isoformat() ) 
    
    return render_template('members/dashboard.html', member=member, upcoming=upcoming)