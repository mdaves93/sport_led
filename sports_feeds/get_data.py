from ohmysportsfeedspy import MySportsFeeds
import os
import logging
from datetime import datetime


class GetData:
    username = "default"
    password = "default"

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.user_name = os.environ['sport_user']
        self.password = os.environ['sport_password']
        self.feed = MySportsFeeds(version='1.2', store_location='/dev/null')
        self.feed.authenticate(self.user_name, self.password)

    def get_scores(self, league, season, wanted_feed, for_date='', return_format='json'):
        if for_date is '':
            for_date = self.format_current_date()
        results = self.feed.msf_get_data(league=league, season=season, feed=wanted_feed,
                                         fordate=for_date, format=return_format,)
        self.logger.debug(results)
        return results

    def format_current_date(self):
        date = datetime.now()
        year = date.year
        month = date.month
        day = date.day
        return f'{year}{month}{day}'


class GetNba(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nba", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)


class GetNhl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nba", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)


class GetNfl(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nba", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)


class GetMlb(GetData):

    def __init__(self):
        GetData.__init__(self)

    def get_current_scores(self, league="nba", season="current", feed='scoreboard'):
        return self.get_scores(league, season, feed)
