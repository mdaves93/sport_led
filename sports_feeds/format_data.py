import logging


class FormatScores(object):

    def __init__(self, scores):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.score_dict = scores

    def format_score_list(self, sport):
        game_list = []
        try:
            game_list = self.score_dict["scoreboard"]["gameScore"]
        except KeyError:
            return game_list
        simple_list = []
        for game in game_list:
            if game["isUnplayed"] == 'true':
                teams = ' {:3s}{:1s}@{:2s}{:3s} '.format(game["game"]["homeTeam"]["Abbreviation"], ' ', ' ',
                                                         game["game"]["awayTeam"]["Abbreviation"])
                simple_list.append(teams)
                time = '{:^12}'.format(game["game"]["time"])
                simple_list.append(time)
            else:
                home_team = self.set_team(game["game"]["homeTeam"]["Abbreviation"], game["homeScore"])
                away_team = self.set_team(game["game"]["awayTeam"]["Abbreviation"], game["awayScore"])
                simple_list.insert(0, '{:3s}:{:2s}{:3s}:{:2s}'.format(home_team.get_name(),
                                                                      home_team.get_score(),
                                                                      away_team.get_name(),
                                                                      away_team.get_score()))
        logging.debug(simple_list)
        simple_list.insert(0, '{:^12}'.format(sport))
        return simple_list

    def set_team(self, name, score):
        return Team(name, score)


class Team:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score


class FormatStats(object):

    def __init__(self, stats):
        self.stat_dict = {}
        self.stats = stats.get("cumulativeplayerstats").get("playerstatsentry")


class FormatNflStats(FormatStats):

    def __init__(self, stats):
        FormatStats.__init__(self, stats)

    def format_all_stats(self):
        self.stat_dict = {**self.format_passing_stats(), **self.format_rushing_stats(),
                          **self.format_receiving_stats(), **self.format_defensive_stats()}
        return self.stat_dict

    def format_passing_stats(self):
        passing_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):

                if player.get("stats").get(stat).get("@category") == "Passing":
                    if passing_stats.get("Passing" + player.get("stats").get(stat).get("@abbreviation")) is None:
                        passing_stats["Passing" + player.get("stats").get(stat).get("@abbreviation")] = []

                    passing_stats["Passing" + player.get("stats").get(stat).get("@abbreviation")].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
        for stat in passing_stats:
            passing_stats[stat] = sorted(passing_stats[stat], key=lambda tup: int(tup[1]), reverse=True)[:5]
        return passing_stats

    def format_rushing_stats(self):
        rushing_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):

                if player.get("stats").get(stat).get("@category") == "Rushing":
                    if rushing_stats.get("Rushing" + player.get("stats").get(stat).get("@abbreviation")) is None:
                        rushing_stats["Rushing" + player.get("stats").get(stat).get("@abbreviation")] = []

                    rushing_stats["Rushing" + player.get("stats").get(stat).get("@abbreviation")].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
        for stat in rushing_stats:
            rushing_stats[stat] = sorted(rushing_stats[stat], key=lambda tup: int(tup[1]), reverse=True)[:5]
        return rushing_stats

    def format_receiving_stats(self):
        receiving_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):

                if player.get("stats").get(stat).get("@category") == "Receiving":
                    if receiving_stats.get("Receiving" + player.get("stats").get(stat).get("@abbreviation")) is None:
                        receiving_stats["Receiving" + player.get("stats").get(stat).get("@abbreviation")] = []

                    receiving_stats["Receiving" + player.get("stats").get(stat).get("@abbreviation")].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
        for stat in receiving_stats:
            receiving_stats[stat] = sorted(receiving_stats[stat], key=lambda tup: int(tup[1]), reverse=True)[:5]
        return receiving_stats

    def format_defensive_stats(self):
        defence_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):
                if stat == "Interceptions":
                    if defence_stats.get("Interceptions") is None:
                        defence_stats["Interceptions"] = []
                    defence_stats["Interceptions"].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))

                if stat == "TackleTotal":
                    if defence_stats.get("TackleTotal") is None:
                        defence_stats["TackleTotal"] = []
                    defence_stats["TackleTotal"].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))

                if stat == "Sacks":
                    if defence_stats.get("Sacks") is None:
                        defence_stats["Sacks"] = []
                    defence_stats["Sacks"].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))

        for stat in defence_stats:
            defence_stats[stat] = sorted(defence_stats[stat], key=lambda tup: int(float(tup[1])), reverse=True)[:5]
        return defence_stats


class FormatMlbStats(FormatStats):

    def __init__(self, stats):
        FormatStats.__init__(self, stats)
        self.max_games = self.max_games_played()
        self.max_innings_pitched = self.max_innings_pitched()
        self.eligible_games = int(self.max_games) * 0.75
        self.eligible_pitcher = float(self.max_innings_pitched) * 0.5

    def format_all_stats(self):
        self.stat_dict = {**self.format_batting_stats(), **self.format_pitching_stats()}
        return self.stat_dict

    def max_games_played(self):
        return max([int(x["stats"]["GamesPlayed"]["#text"]) for x in self.stats])

    def max_innings_pitched(self):
        max_games_started = 0
        pitching_list = set([])
        for player in self.stats:
            if player.get("stats").get("InningsPitched"):
                pitching_list.add(float(player.get("stats").get("InningsPitched").get("#text")))
        max_games_started = max(pitching_list)
        return max_games_started

    def format_batting_stats(self):
        batting_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):
                if player.get("stats").get(stat).get("@category") == "Batting":
                    if batting_stats.get(stat) is None:
                        if stat is "BatterStrikeouts":
                            batting_stats["BatterSO"] = []
                        else:
                            batting_stats[stat] = []
                    if float(player.get("stats").get("GamesPlayed").get("#text")) >= self.eligible_games:
                        batting_stats[stat].append((player.get("player").get("LastName"),
                                                    player.get("stats").get(stat).get("#text")))
        for stat in batting_stats:
            batting_stats[stat] = sorted(batting_stats[stat], key=lambda tup: float(tup[1]), reverse=True)[:5]
        return batting_stats

    def format_pitching_stats(self):
        pitching_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):
                if player.get("stats").get(stat).get("@category") == "Pitching":
                    if pitching_stats.get(stat) is None:
                        if stat is "PitcherStrikeouts":
                            pitching_stats["PitcherSO"] = []
                        else:
                            pitching_stats[stat] = []
                    if stat == "EarnedRunAvg" and float(player.get("stats").get("InningsPitched")
                                                        .get("#text")) > self.eligible_pitcher:
                        pitching_stats[stat].append(
                            (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
                        continue
                    elif stat == "EarnedRunAvg":
                        continue
                    pitching_stats[stat].append(
                        (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
        for stat in pitching_stats:
            if stat == "EarnedRunAvg":
                pitching_stats[stat] = sorted(pitching_stats[stat], key=lambda tup: float(tup[1]), reverse=False)[:5]
            else:
                pitching_stats[stat] = sorted(pitching_stats[stat], key=lambda tup: float(tup[1]), reverse=True)[:5]
        return pitching_stats


class FormatNbaStats(FormatStats):

    def __init__(self, stats):
        FormatStats.__init__(self, stats)

    def format_all_stats(self):
        self.stat_dict = {**self.format_nba_stats()}
        return self.stat_dict

    def format_nba_stats(self):
        nba_stats = {}
        for player in self.stats:
            for stat in player.get("stats"):

                if nba_stats.get(stat) is None:
                    nba_stats[stat] = []

                nba_stats[stat].append(
                    (player.get("player").get("LastName"), player.get("stats").get(stat).get("#text")))
        for stat in nba_stats:
            nba_stats[stat] = sorted(nba_stats[stat], key=lambda tup: int(float(tup[1])), reverse=True)[:5]
        return nba_stats


class FormatNhlStats(FormatStats):

    def __init__(self, stats):
        FormatStats.__init__(self, stats)

    def format_all_stats(self):
        self.stat_dict = {**self.format_nhl_stats()}
        return self.stat_dict

    def format_nhl_stats(self):
        nhl_stats = {}
        for player in self.stats:
            for stat in player.get("stats").get("stats"):
                if nhl_stats.get(stat) is None:
                    nhl_stats[stat] = []

                nhl_stats[stat].append(
                    (player.get("player").get("LastName"), player.get("stats").get("stats").get(stat).get("#text")))
        for stat in nhl_stats:
            nhl_stats[stat] = sorted(nhl_stats[stat], key=lambda tup: int(float(tup[1])), reverse=True)[:5]
        return nhl_stats
