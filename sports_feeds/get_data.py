import json

from ohmysportsfeedspy import MySportsFeeds
import os
import logging
import tempfile
from datetime import datetime


class GetData:

    def __init__(self, stats=None):
        self.temp_file = tempfile.TemporaryFile()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.user_name = os.environ['sport_user']
        self.password = os.environ['sport_password']
        self.feed = MySportsFeeds(version="1.1", store_type=None)
        self.feed.authenticate(self.user_name, self.password)
        self.stats = stats
        self.stat_data = None
        self.score_data = None

    def get_data(self, league, season, wanted_feed, for_date='', return_format='json', player_stats=''):
        if for_date is '':
            for_date = self.format_current_date()
        results = self.feed.msf_get_data(league=league, season=season, feed=wanted_feed,
                                         fordate=for_date, format=return_format, force=True,
                                         playerstats=player_stats)
        self.logger.info(player_stats)
        self.logger.debug(results)
        return json.dumps(results)

    def format_current_date(self):
        date = datetime.now()
        year = date.year
        month = '{:02d}'.format(date.month)
        day = '{:02d}'.format(date.day)
        return f'{year}{month}{day}'


class GetNba(GetData):

    def __init__(self, stats=None):
        GetData.__init__(self, stats)

    def get_current_scores(self, league="nba", season="latest", feed='scoreboard'):
        self.score_data = self.get_data(league, season, feed)
        return json.loads(self.score_data)

    def get_stats(self, league="nba", season="latest", feed='cumulative_player_stats'):
        self.stat_data = self.get_data(league=league, season=season, wanted_feed=feed, player_stats=self.stats)
        return json.loads(self.stat_data)

    def get_chosen_data(self):
        self.get_current_scores()
        self.get_stats()


class GetNhl(GetData):

    def __init__(self, stats=None):
        GetData.__init__(self, stats)

    def get_current_scores(self, league="nhl", season="latest", feed='scoreboard'):
        self.score_data = self.get_data(league, season, feed)
        return json.loads(self.score_data)

    def get_stats(self, league="nhl", season="latest", feed='cumulative_player_stats'):
        self.stat_data = self.get_data(league=league, season=season, wanted_feed=feed, player_stats=self.stats)
        return json.loads(self.stat_data)

    def get_chosen_data(self):
        self.get_current_scores()
        self.get_stats()


class GetNfl(GetData):

    def __init__(self, stats=None):
        GetData.__init__(self, stats)

    def get_current_scores(self, league="nfl", season="latest", feed='scoreboard'):
        self.score_data = self.get_data(league, season, feed)
        return json.loads(self.score_data)

    def get_stats(self, league="nfl", season="latest", feed='cumulative_player_stats'):
        self.stat_data = self.get_data(league=league, season=season, wanted_feed=feed, player_stats=self.stats)
        return json.loads(self.stat_data)

    def get_chosen_data(self):
        self.get_current_scores()
        self.get_stats()


class GetMlb(GetData):

    def __init__(self, stats=None):
        GetData.__init__(self, stats)

    def get_current_scores(self, league="mlb", season="latest", feed='scoreboard'):
        self.score_data = self.get_data(league, season, feed)
        return json.loads(self.score_data)

    def get_stats(self, league="mlb", season="latest", feed='cumulative_player_stats'):
        self.stat_data = self.get_data(league=league, season=season, wanted_feed=feed, player_stats=self.stats)
        return json.loads(self.stat_data)

    def get_chosen_data(self):
        self.get_current_scores()
        self.get_stats()
