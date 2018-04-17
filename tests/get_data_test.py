import unittest

from unittest.mock import Mock
from unittest.mock import patch
import json
import ohmysportsfeedspy
from sports_feeds.get_data import GetData
from sports_feeds.get_data import GetNba
from sports_feeds.get_data import GetNhl
from sports_feeds.get_data import GetNfl
from sports_feeds.get_data import GetMlb


class TestGetData(unittest.TestCase):

    def setUp(self):
        self.data = GetData()

    def test_feed_is_sport_object(self):
        self.assertIsInstance(self.data.feed, ohmysportsfeedspy.MySportsFeeds)


class TestGetNbaData(unittest.TestCase):

    def setUp(self):
        self.test_nba = GetNba()

    def test_auth(self):
        self.assertEqual(type(self.test_nba.feed.api_instance.auth), tuple)

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_basic_api_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nba.json'))
        test_scores = self.test_nba.get_data("nba", "latest", "scoreboard")
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_get_nba_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nba.json'))
        test_scores = self.test_nba.get_current_scores()
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")


class TestGetNflData(unittest.TestCase):

    def setUp(self):
        self.test_nfl = GetNfl()

    def test_auth(self):
        self.assertEqual(type(self.test_nfl.feed.api_instance.auth), tuple)

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_basic_api_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nfl.json'))
        test_scores = self.test_nfl.get_data("nfl", "latest", "scoreboard")
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_get_nfl_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nfl.json'))
        test_scores = self.test_nfl.get_current_scores()
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")


class TestGetNhlData(unittest.TestCase):

    def setUp(self):
        self.test_nhl = GetNhl()

    def test_auth(self):
        self.assertEqual(type(self.test_nhl.feed.api_instance.auth), tuple)

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_basic_api_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nhl.json'))
        test_scores = self.test_nhl.get_data("nhl", "latest", "scoreboard")
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_get_nfl_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_nhl.json'))
        test_scores = self.test_nhl.get_current_scores()
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")


class TestGetNflData(unittest.TestCase):

    def setUp(self):
        self.test_mlb = GetNfl()

    def test_auth(self):
        self.assertEqual(type(self.test_mlb.feed.api_instance.auth), tuple)

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_basic_api_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_mlb.json'))
        test_scores = self.test_mlb.get_data("mlb", "latest", "scoreboard")
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")

    @patch('sports_feeds.get_data.MySportsFeeds.msf_get_data')
    def test_get_mlb_call(self, mock_get):
        mock_get.return_value = json.load(open('resources/test_data_mlb.json'))
        test_scores = self.test_mlb.get_current_scores()
        self.assertEqual(test_scores['scoreboard']['lastUpdatedOn'], "2018-02-02 2:12:23 AM")



if __name__ == '__main__':
    unittest.main()
