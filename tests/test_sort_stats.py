import json
import unittest

import sports_feeds.format_data as stats


class TestSortStats(unittest.TestCase):

    def setUp(self, stat_path):
        with open(stat_path) as test_data:
            self.test_data = json.loads(test_data.read())
            test_data.close()


class TestNflStats(TestSortStats):

    STAT_PATH = "resources/nfl_test_stats.json"

    def setUp(self, stat_path=STAT_PATH):
        TestSortStats.setUp(self, self.STAT_PATH)
        self.nfl = stats.FormatNflStats(self.test_data)

    def test_format_passing(self):
        self.assertTrue(self.nfl.format_passing_stats())

    def test_format_rushing(self):
        self.assertTrue(self.nfl.format_rushing_stats())

    def test_format_receiving(self):
        self.assertTrue(self.nfl.format_receiving_stats())

    def test_format_defense(self):
        self.assertTrue(self.nfl.format_defensive_stats())

    def test_format_all(self):
        self.assertTrue(self.nfl.format_all_stats())

class TestMlbStats(TestSortStats):

    STAT_PATH = "resources/mlb_test_stats.json"

    def setUp(self, stat_path=STAT_PATH):
        TestSortStats.setUp(self, self.STAT_PATH)
        self.mlb = stats.FormatMlbStats(self.test_data)

    def test_format_batting(self):
        self.assertTrue(self.mlb.format_batting_stats())

    def test_format_pitching(self):
        self.assertTrue(self.mlb.format_pitching_stats())

    def test_format_all(self):
        self.assertTrue(self.mlb.format_all_stats())

    def test_max_games(self):
        print(self.mlb.max_games_played())

class TestNbaStats(TestSortStats):

    STAT_PATH = "resources/nba_test_stats.json"

    def setUp(self, stat_path=STAT_PATH):
        TestSortStats.setUp(self, self.STAT_PATH)
        self.nba = stats.FormatNbaStats(self.test_data)

    def test_format_nba_stats(self):
        self.assertTrue(self.nba.format_nba_stats())

    def test_format_all(self):
        self.assertTrue(self.nba.format_all_stats())


class TestNhlStats(TestSortStats):

    STAT_PATH = "resources/nhl_test_stats.json"

    def setUp(self, stat_path=STAT_PATH):
        TestSortStats.setUp(self, self.STAT_PATH)
        self.nhl = stats.FormatNhlStats(self.test_data)

    def test_format_nba_stats(self):
        self.assertTrue(self.nhl.format_nhl_stats())

    def test_format_all(self):
        self.assertTrue(self.nhl.format_all_stats())
