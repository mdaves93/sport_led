import json
import sports_feeds.parse_data
import unittest
from unittest.mock import Mock
from unittest.mock import patch


class TestParseScores(unittest.TestCase):

    def setUp(self):
        test_data = open('resources/test_data_nfl.json')
        self.data = sports_feeds.parse_data.FeedData(test_data)
        test_data.close()

    def test_get_score_list(self):
        scores = self.data.get_score_list()
        print(scores[0].game.awayTeam.Name)
        self.assertIsInstance(scores, list)

    def test_set_team(self):
        team = self.data.set_team('name', 'score')
        self.assertIsInstance(team, sports_feeds.parse_data.Team)
        self.assertEqual(team.name, 'name')
        self.assertEqual(team.score, 'score')

    def test_simplify_list(self):
        simple_list = self.data.format_score_list()
        self.assertIsInstance(simple_list, list)
        self.assertIsInstance(simple_list[0], str)

