
class AbbreviationConverter:
    abbreviation_dictionary = {"BS": "Blocked Shots",
                               "Blocked Shots": "BS",
                               "AST": "Assists",
                               "Assists": "AST",
                               "PTS": "Points",
                               "Points": "PTS",
                               "REB": "Rebound",
                               "Rebound": "REB",
                               "STL": "Steal",
                               "Steal": "STL",
                               "3PM": "3-Pointers",
                               "3-Pointers": "3PM",
                               "GP": "Games Played",
                               "Games Played": "GP",
                               "Passing Yards": "PY",
                               "PY": "Passing Yards",
                               "Passing TD": "PTD",
                               "PTD": "Passing TD",
                               "Receiving TD": "RTD",
                               }


    def convert(self, stat):
        return self.abbreviation_dictionary.get(stat)