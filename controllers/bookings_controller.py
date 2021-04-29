from datetime import datetime
from flask import Flask, Blueprint, redirect, render_template, request, url_for
import pdb
from models.booking import Booking
from models.activity import Activity
from models.member import Member
import repositories.member_repo as member_repo
import repositories.activity_repo as act_repo
import repositories.booking_repo as booking_repo

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("/bookings/<act_id>_<member_id>_add")
def make_booking(act_id, member_id):
    member = member_repo.select(member_id)
    activity = act_repo.select(act_id)
    booking_repo.save(Booking(member, activity))
    return redirect(url_for('activities.view_activity', id=member_id, activity_id=act_id))

@bookings_bp.route("/bookings/<id>/view")
def view_member_bookings(id):
    activities = booking_repo.select_activities_of_member(id)
    return render_template("bookings/view.html", id=id, activities=activities)
