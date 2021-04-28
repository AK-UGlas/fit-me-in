from flask import Flask, render_template

from utilities.utilities import date_string

from controllers.members_controller import members_bp
from controllers.activities_controller import act_bp
from controllers.bookings_controller import bookings_bp

import repositories.activity_repo as act_repo

app = Flask(__name__)

app.register_blueprint(members_bp)
app.register_blueprint(act_bp)
app.register_blueprint(bookings_bp)

@app.route("/")
def home():
    return render_template('index.html', title="FitMeIn | Book your next fitness class now")

@app.route("/admin-dash")
def admin():
    admin_id = "admin"
    date, date_str = date_string()
    upcoming = act_repo.upcoming(date)

    return render_template("admin.html", admin_id=admin_id, upcoming=upcoming, today=date_str)

@app.route("/about")
def about():
    return render_template("about.html", title="FitMeIn | About us")

if __name__ == '__main__':
    app.run(debug=True)