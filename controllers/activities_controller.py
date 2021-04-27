from datetime import datetime, timedelta
from flask import Flask, Blueprint, redirect, render_template, request, url_for
import dateutil

from models.activity import Activity
from models.location import Location
import repositories.activity_repo as act_repo
import repositories.location_repo as loc_repo

act_bp = Blueprint("activities", __name__)

# time formatting helper function
def format_time():
    # get current time and round to the coming hour using a timedelta object
    now = datetime.now().replace(microsecond=0, second=0)
    delta = timedelta(minutes = 60 - now.minute)

    # arbitrary cutoff for scheduling a new activity
    # e.g. must be within 5 min of the coming hour
    cutoff = 5 # normally we'd place this in a separate file with constant values
    
    if 60 - now.minute < cutoff:
        # add another hour
        delta = delta + timedelta(minutes=60)
    display_time = now + delta

    # activities can only be scheduled between 08:00 and 22:00
    target_hour = display_time.hour
    if target_hour > 21:
        display_time = display_time + timedelta(minutes=(24 - target_hour + 8) * 60)
    elif 0 <= target_hour < 8:
        display_time = display_time + timedelta(minutes=(8 - target_hour) * 60)

    return display_time

#new activity form
@act_bp.route("/activities/add")
def new_activity():
    # get the locations the gym has to load into form
    locations = loc_repo.select_all()
    display_time = format_time()
    max_time = display_time + timedelta(weeks=2)

    return render_template("activities/add.html", title="--admin-- | add new activity", 
                            locs=locations, displaytime=display_time.isoformat(), 
                            maxtime=max_time.isoformat)

# create newly added activity
@act_bp.route("/activities/add", methods=['POST'])
def create_activity():
    name = request.form['name']
    dt = dateutil.parser.isoparse(request.form['time'])
    location = loc_repo.select(request.form['location'])
    activity = act_repo.save(Activity(name, dt, location))
    
    #TODO add this functionality to link above
    message = "Activity created successfully!"
    if activity is None:
        message = "Cannot add activity. Time clash detected"

    return redirect("/activities/add")
