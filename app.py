from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def home():
    page_type = "home"

    return render_template('main.html', page_type=page_type)


@app.route('/nhl')
def nhl():
    stats = ["Goals", "Assists", "Points"]

    return render_template('main.html', stats=stats)

@app.route('/nfl')
def nfl():
    stats = ["Passing Yards", "Passing TD", "Rushing Yards", "Rushing TD" "Receiving Yards", "Receiving TD"]

    return render_template('main.html', stats=stats)


@app.route('/nba')
def nba():
    stats = ["Points", "Assists", "Steals", "Blocks"]

    return render_template('main.html', stats=stats)

@app.route('/mlb')
def mlb():
    stats = ["Batting Avg", "Home Runs", "RBI", "Hits", "BStrikeouts", "BWalks", "Steals", "ERA", "Wins", "PStrikeouts", "PWalks" "Saves"]

    return render_template('main.html', stats=stats)


if __name__ == '__main__':
    app.run(debug=True)
