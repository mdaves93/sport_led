import operator

import sports_feeds.get_data
from collections import namedtuple
import json
import logging


def _json_object_hook(d):
    return namedtuple('X', d.keys(), rename=True)(*d.values())


abbreviation_dictionary = {"BS": "Blocked Shots",
                           "AST": "Assists",
                           "PTS": "Points",
                           "REB": "Rebound",
                           "STL": "Steal",
                           "3PM": "3-Pointers",
                           "GP": "Games Played"}


class FeedData:

    def __init__(self, data):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.data = json.loads(str(data), object_hook=_json_object_hook)

    def get_score_list(self):
        return self.data.scoreboard.gameScore

    #Returns object of player objects
    def get_stat_list(self, stat):
        # print(self.data.cumulativeplayerstats.playerstatsentry)
        return self.data.cumulativeplayerstats.playerstatsentry

    def set_team(self, name, score):
        return Team(name, score)

    def format_score_list(self, sport):
        game_list = self.get_score_list()
        simple_list = []
        for game in game_list:
            if game.isUnplayed == 'true':
                teams = ' {:3s}{:4s}{:3s} '.format(game.game.homeTeam.Abbreviation, ' ', game.game.awayTeam.Abbreviation)
                simple_list.append(teams)
                time = '{:^12}'.format(game.game.time)
                simple_list.append(time)
            else:
                home_team = self.set_team(game.game.homeTeam.Abbreviation, game.homeScore)
                away_team = self.set_team(game.game.awayTeam.Abbreviation, game.awayScore)
                simple_list.insert(0, '{:3s}:{:2s}{:3s}:{:2s}'.format(home_team.get_name(),
                                                                      home_team.get_score(),
                                                                      away_team.get_name(),
                                                                      away_team.get_score()))
        logging.debug(simple_list)
        simple_list.insert(0, '{:^12}'.format(sport))
        return simple_list

    def format_stat_list(self):
        player_list = self.get_stat_list('')
        simple_list = []
        stat_dict = {}
        for player in player_list:

            current_list = []
            current_stat = ''
            for stat in player.stats:
                if str(stat[-2]) not in stat_dict:
                    stat_dict[str(stat[-2])] = []
                stat_dict[str(stat[-2])].append((player.player.LastName, stat[-2], stat[-1]))
        top_ten = []
        stats_list = []
        for stat in stat_dict:
            top_ten = list(sorted(stat_dict[stat], key=lambda sort_stat: int(sort_stat[-1]), reverse=True)[:10])
            # print('{}  {}'.format(stat, top_ten))
            if top_ten[0][1] == 'GP':
                continue
            stats_list.append("{:^12}".format(abbreviation_dictionary.get(str(top_ten[0][1]))))
            for stats in top_ten:
                last_name = stats[0][:7]
                value = stats[2]
                stat_string = '{:7s} {:4s}'.format(last_name, value)
                stats_list.append(stat_string)
        print(stats_list)

        return simple_list

    def list_to_string(self, list_data):
        this_string = ''
        for item in list_data:
            this_string = this_string + item
        print(this_string)
        return this_string


class Team:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score
