from flask import Flask
from flask import render_template
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
                      ("BatterWalks", "BB"), ("Steals", "STL"), ("ERA", "ERA"), ("Wins", "W"), ("PitcherSO", "SO"),
                      ("PitcherWalks", "BB"), ("Saves", "SV")],
              "NBA": [("Points", "P"), ("Assists", "AST"), ("Steals", "STL"), ("Blocks", "BS"), ("Rebounds", "REB"),
                      ("3 Points Made", "3PM")],
              "NHL": [("Goals", "G"), ("Assists", "A"), ("Points", "Pts"), ("HatTricks", "Hat"), ("Shut Outs", "SO")]}

    return render_template('main.html', page_type=page_type, sports=sports)


@app.route('/submit', methods=["POST"])
def submit():
    print(request.form.getlist("MLB"))
    print(request.form.getlist("MLBScore"))
    
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
