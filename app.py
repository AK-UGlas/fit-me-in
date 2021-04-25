from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    render_template('index.html', title="FitMeIn | Book your next fitness class now")

if __name__ == '__main__':
    app.run(debug=True)