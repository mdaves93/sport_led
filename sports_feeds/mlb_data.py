import ohmysportsfeedspy
import os
import logging

class MlbData():

    def __init__(self):
        self.logger = logging.basicConfig(level=logging.DEBUG)
        self.user_name = os.environ['sport_user']
        self.password = os.environ['sport_password']
        return

    def get_new_feed(self):
        mlb_feed = ohmysportsfeedspy.MySportsFeeds(version='1.2')
        mlb_feed.authenticate(self.user_name, self.password)
        return mlb_feed

