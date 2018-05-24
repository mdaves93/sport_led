from flask import Flask
from flask import render_template
import json
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    page_type = "home"
    sports = {"NFL": [("PassingYds", "YDS"), ("PassingTD", "TD"), ("RushingYds", "YDS"), ("RushingTD", "TD"),
                      ("ReceivingYds", "YDS"), ("ReceivingTD", "TD"), ("Interceptions", "INT"),
                      ("Tackles", "Total"), ("Sacks", "Sacks")],
              "MLB": [("BattingAvg", "AVG"), ("HomeRuns", "HR"), ("RBI", "RBI"), ("Hits", "H"), ("BatterSO", "SO"),
                      ("BatterWalks", "BB"), ("StolenBases", "SB"), ("ERA", "ERA"), ("Wins", "W"), ("PitcherSO", "SO"),
                      ("PitcherWalks", "BB"), ("Saves", "SV")],
              "NBA": [("Points", "PTS"), ("Assists", "AST"), ("Steals", "STL"), ("Blocks", "BS"), ("Rebounds", "REB"),
                      ("3 Points Made", "3PM")],
              "NHL": [("Goals", "G"), ("Assists", "A"), ("Points", "PTS"), ("HatTricks", "Hat"), ("Shut Outs", "SO")]}

    return render_template('main.html', page_type=page_type, sports=sports)


@app.route('/submit', methods=["POST"])
def submit():
    print(request.form.getlist("MLB"))
    print(request.form.getlist("MLBScore"))
    if request.form.getlist("MLB"):
        mlb_stats = ",".join(set(request.form.getlist("MLB")))
    else:
        mlb_stats = None
    if request.form.getlist("NFL"):
        nfl_stats = ",".join(set(request.form.getlist("NFL")))
    else:
        nfl_stats = None
    if request.form.getlist("NBA"):
        nba_stats = ",".join(set(request.form.getlist("NBA")))
    else:
        nba_stats = None
    if request.form.getlist("NHL"):
        nhl_stats = ",".join(set(request.form.getlist("NHL")))
    else:
        nhl_stats = None

    json_string = {"MLB": {"scores": request.form.getlist("MLBScore"),
                        "stats": mlb_stats},
                "NFL": {"scores": request.form.getlist("NFLScore"),
                        "stats": nfl_stats},
                "NBA": {"scores": request.form.getlist("NBAScore"),
                        "stats": nba_stats},
                "NHL": {"scores": request.form.getlist("NHLScore"),
                        "stats": nhl_stats}
                }

    with open('resources/parameters.json', 'w') as f:
        json.dump(json_string, f)
    return home()


# @app.route('/nhl', methods=["POST", "GET"])
# def nhl():
#     stats = ["Goals", "Assists", "Points"]
#
#     return render_template('main.html', stats=stats)
#
#
# @app.route('/nfl')
# def nfl():
#     stats = ["Passing Yards", "Passing TD", "Rushing Yards", "Rushing TD" "Receiving Yards", "Receiving TD"]
#
#     return render_template('main.html', stats=stats)
#
#
# @app.route('/nba')
# def nba():
#     stats = ["Points", "Assists", "Steals", "Blocks"]
#
#     return render_template('main.html', stats=stats)
#
#
# @app.route('/mlb')
# def mlb():
#     stats = ["Batting Avg", "Home Runs", "RBI", "Hits", "BStrikeouts", "BWalks", "Steals", "ERA", "Wins", "PStrikeouts",
#              "PWalks" "Saves"]
#
#     return render_template('main.html', stats=stats)


# @app.route('/change_display')
# def change_display(display_objects):
#     pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
