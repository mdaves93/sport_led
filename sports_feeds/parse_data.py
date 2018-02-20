import sports_feeds.get_data
from collections import namedtuple
import json
import logging


def _json_object_hook(d):
    return namedtuple('X', d.keys(), rename=True)(*d.values())


class FeedData:

    def __init__(self, data):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        print(str(data))
        self.data = json.loads(str(data), object_hook=_json_object_hook)

    def get_game_list(self):
        return self.data.scoreboard.gameScore

    def set_team(self, name, score):
        return Team(name, score)

    def simplify_list(self):
        game_list = self.get_game_list()
        simple_list = []
        for game in game_list:
            print(game.isUnplayed)
            if game.isUnplayed == 'true':
                simple_list.append('{:3s}      {:3s}{}'.format(game.game.homeTeam.Abbreviation,
                                                               game.game.awayTeam.Abbreviation,
                                                               game.game.time))
            else:
                home_team = self.set_team(game.game.homeTeam.Abbreviation, game.homeScore)
                away_team = self.set_team(game.game.awayTeam.Abbreviation, game.awayScore)
                simple_list.insert(0, '{:3s}:{:2s}{:3s}:{:2s}'.format(home_team.get_name(),
                                                                       home_team.get_score(),
                                                                       away_team.get_name(),
                                                                       away_team.get_score()))
        logging.debug(simple_list)
        return simple_list


class Team:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score
