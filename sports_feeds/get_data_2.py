import json

from ohmysportsfeedspy import MySportsFeeds
import os
import logging
import tempfile
from datetime import datetime


class GetData:

    def __init__(self, stats):
        self.temp_file = tempfile.TemporaryFile()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.user_name = os.environ['sport_user']
        self.password = os.environ['sport_password']
        self.feed = MySportsFeeds(version="1.2", store_type=None)
        self.feed.authenticate(self.user_name, self.password)
        self.current_data = None
        self.stats = stats

    def get_data(self, league, wanted_feed, for_date='', season='current', return_format='json', player_stats=''):
        if for_date is '':
            for_date = self.format_current_date()
        # try:
        results = self.feed.msf_get_data(league=league, season=season, feed=wanted_feed,
                                         fordate=for_date, format=return_format, force=True,
                                         playerstats=player_stats)
        # except Exception:
        #     return None
        self.current_data = results
        self.logger.debug(results)
        return json.dumps(results)

    def format_current_date(self):
        date = datetime.now()
        year = date.year
        month = '{:02d}'.format(date.month)
        day = '{:02d}'.format(date.day)
        return f'{year}{month}{day}'

