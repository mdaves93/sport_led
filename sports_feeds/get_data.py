import json

from ohmysportsfeedspy import MySportsFeeds
import os
import logging
import tempfile
from datetime import datetime


class GetData:

    def __init__(self):
        self.temp_file = tempfile.TemporaryFile()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.user_name = os.environ['sport_user']
        self.password = os.environ['sport_password']
        self.feed = MySportsFeeds(version="1.2", store_type=None)
        self.feed.authenticate(self.user_name, self.password)

    def get_data(self, league, season, wanted_feed, for_date='', return_format='json', player_stats=''):
        if for_date is '':
            for_date = self.format_current_date()
        # try:
        results = self.feed.msf_get_data(league=league, season=season, feed=wanted_feed,
                                         fordate=for_date, format=return_format, force=True,
                                         playerstats=player_stats)
        # except Exception:
        #     return None

        self.logger.debug(results)
        return json.dumps(results)

    def format_current_date(self):
        date = datetime.now()
        year = date.year
        month = '{:02d}'.format(date.month)
        day = '{:02d}'.format(date.day)
        return f'{year}{month}{day}'


class GetNba(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nba", season="current", feed='scoreboard'):
        return self.get_data(league, season, feed)

    def get_stats(self, league="nba", season="current", feed='cumulative_player_stats', player_stats="PTS,AST,REB,BS,STL,3PM"):
        return self.get_data(league=league, season=season, wanted_feed=feed, player_stats=player_stats)


class GetNhl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nhl", season="current", feed='scoreboard'):
        return self.get_data(league, season, feed)

    def get_stats(self):
        return True


class GetNfl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nfl", season="current", feed='scoreboard'):
        return self.get_data(league, season, feed)

    def get_stats(self):
        return True


class GetMlb(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="mlb", season="current", feed='scoreboard'):
        return self.get_data(league, season, feed)

    def get_stats(self):
        return True
