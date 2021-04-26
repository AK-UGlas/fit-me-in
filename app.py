from flask import Flask, render_template

from controllers.members_controller import members_bp
from controllers.activities_controller import act_bp

app = Flask(__name__)

app.register_blueprint(members_bp)
app.register_blueprint(act_bp)

@app.route("/")
def home():
    return render_template('index.html', title="FitMeIn | Book your next fitness class now")

if __name__ == '__main__':
    app.run(debug=True)