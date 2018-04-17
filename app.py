from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    page_type = "home"
    sports = {"NFL": [("Passing Yards", "YDS"), ("Passing TD", "TD"), ("Rushing Yards", "YDS"), ("Rushing TD", "TD"),
                      ("Receiving Yards", "YDS"), ("Receiving TD", "TD"), ("Interceptions")],
              "MLB": [("Batting Avg", "AVG"), ("Home Runs", "HR"), ("RBI", "RBI"), ("Hits", "H"), ("BStrikeouts", "SO"),
                      ("BWalks", "BB"), ("Steals", "STL"), ("ERA", "ERA"), ("Wins", "W"), ("PStrikeouts", "SO"),
                      ("PWalks", "BB"), ("Saves", "SV")],
              "NBA": [("Points", "P"), ("Assists", "AST"), ("Steals", "STL"), ("Blocks", "BS"), ("Rebounds", "REB"),
                      ("3 Points Made", "3PM")],
              "NHL": [("Goals", "G"), ("Assists", "A"), ("Points", "Pts"), ("Hat Tricks", "Hat"), ("Shut Outs", "SO")]}

    return render_template('main.html', page_type=page_type, sports=sports)


@app.route('/nhl', methods=["POST", "GET"])
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


@app.route('/change_display')
def change_display(display_objects):

    pass


if __name__ == '__main__':
    app.run(debug=True)
