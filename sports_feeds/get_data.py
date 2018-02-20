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
        self.feed = MySportsFeeds(version="1.2", store_type=None, store_location='results/')
        self.feed.authenticate(self.user_name, self.password)

    def get_scores(self, league, season, wanted_feed, for_date='', return_format='json'):
        if for_date is '':
            for_date = self.format_current_date()
        print(for_date)
        results = self.feed.msf_get_data(league=league, season=season, feed=wanted_feed,
                                         fordate=for_date, format=return_format, force=True)
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
        return self.get_scores(league, season, feed)


class GetNhl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nhl", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)


class GetNfl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nfl", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)


class GetMlb(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="mlb", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)
