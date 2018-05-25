import json
import sports_feeds.type_changer
import unittest
from unittest.mock import Mock
from unittest.mock import patch


class TestParseScores(unittest.TestCase):

    def setUp(self):
        test_file = open('resources/test_data_nfl.json')
        test_data = test_file.read()
        self.data = sports_feeds.type_changer.ParseData(test_data)
        test_file.close()

    def test_get_score_list(self):
        scores = self.data.get_score_list()
        self.assertIsInstance(scores, list)

    def test_set_team(self):
        team = self.data.set_team('name', 'score')
        self.assertIsInstance(team, sports_feeds.type_changer.Team)
        self.assertEqual(team.name, 'name')
        self.assertEqual(team.score, 'score')

    def test_simplify_list(self):
        simple_list = self.data.format_score_list("NFL")
        self.assertIsInstance(simple_list, list)
        self.assertIsInstance(simple_list[0], str)

class TestParseStats(unittest.TestCase):

    def setUp(self):
        test_file = open('resources/nfl_test_stats.json')
        test_data = test_file.read()
        self.data = sports_feeds.type_changer.ParseData(test_data)
        test_file.close()
        self.stat_dict = {'PassingAtt': [('Brady', '139'), ('Foles', '106'), ('Keenum', '88'), ('Bortles', '85'), ('Brees', '73')], 'PassingComp': [('Brady', '89'), ('Foles', '77'), ('Keenum', '53'), ('Bortles', '49'), ('Brees', '48')], 'PassingPct': [('Burton', '100.0'), ('Smith', '72.7'), ('Foles', '72.6'), ('Brees', '65.8'), ('Ryan', '65.2')], 'PassingYds': [('Brady', '1132'), ('Foles', '971'), ('Brees', '670'), ('Bortles', '594'), ('Keenum', '589')], 'PassingAvg': [('Amendola', '10.0'), ('Brees', '9.2'), ('Foles', '9.2'), ('Newton', '8.7'), ('Brady', '8.1')], 'PassingYards/Att': [('Amendola', '10.0'), ('Brees', '9.2'), ('Foles', '9.2'), ('Newton', '8.7'), ('Brady', '8.1')], 'PassingTD': [('Brady', '8'), ('Foles', '6'), ('Brees', '5'), ('Roethlisberger', '5'), ('Mariota', '4')], 'PassingTD%': [('Burton', '100.0'), ('Roethlisberger', '8.6'), ('Brees', '6.8'), ('Smith', '6.1'), ('Mariota', '5.9')], 'PassingInt': [('Brees', '3'), ('Keenum', '3'), ('Foles', '1'), ('Mariota', '1'), ('Peterman', '1')], 'PassingInt%': [('Peterman', '33.3'), ('Brees', '4.1'), ('Keenum', '3.4'), ('Taylor', '2.7'), ('Roethlisberger', '1.7')], 'PassingLng': [('Brees', '80'), ('Keenum', '61'), ('Newton', '56'), ('Foles', '55'), ('Ryan', '52')], 'Passing20+': [('Brady', '18'), ('Foles', '12'), ('Bortles', '10'), ('Keenum', '8'), ('Brees', '7')], 'Passing40+': [('Foles', '4'), ('Brady', '3'), ('Bortles', '2'), ('Brees', '2'), ('Roethlisberger', '2')], 'PassingSacks': [('Mariota', '11'), ('Ryan', '6'), ('Brady', '4'), ('Newton', '4'), ('Smith', '4')], 'PassingSackY': [('Mariota', '69'), ('Roethlisberger', '59'), ('Newton', '43'), ('Ryan', '35'), ('Brees', '23')], 'PassingQBRating': [('Burton', '118.8'), ('Smith', '116.2'), ('Foles', '115.7'), ('Roethlisberger', '110.5'), ('Brady', '108.6')], 'RushingAtt': [('Fournette', '70'), ('Ajayi', '42'), ('Henry', '35'), ('Lewis', '33'), ('Blount', '29')], 'RushingYds': [('Fournette', '242'), ('Ajayi', '184'), ('Henry', '184'), ('Lewis', '135'), ('Blount', '130')], 'RushingAvg': [('Hill', '14.0'), ('Jones', '13.0'), ('Ginn', '11.0'), ('Thompson', '9.0'), ('Roethlisberger', '8.0')], 'RushingTD': [('Fournette', '4'), ('Blount', '3'), ('White', '3'), ('Bolden', '1'), ('Freeman', '1')], 'RushingLng': [('Blount', '36'), ('Henry', '35'), ('Gurley', '33'), ('Stewart', '29'), ('Ajayi', '26')], 'Rushing1stDowns': [('Fournette', '15'), ('Ajayi', '8'), ('Blount', '8'), ('Coleman', '8'), ('Henry', '6')], 'Rushing1stDowns%': [('Ginn', '100.0'), ('Ham', '100.0'), ('Hill', '100.0'), ('Jones', '100.0'), ('Line', '100.0')], 'Rushing20+': [('Bell', '2'), ('Blount', '2'), ('Gurley', '2'), ('Henry', '2'), ('Agholor', '1')], 'Rushing40+': [('Abbrederis', '0'), ('Abdullah', '0'), ('Adams', '0'), ('Adams', '0'), ('Adams', '0')], 'RushingFum': [('Ajayi', '1'), ('Bortles', '1'), ('Foles', '1'), ('Henry', '1'), ('Peterman', '1')], 'ReceivingTgt': [('Amendola', '33'), ('Gronkowski', '27'), ('Jones', '26'), ('Diggs', '22'), ('Ertz', '22')], 'ReceivingRec': [('Amendola', '26'), ('Ertz', '18'), ('Jones', '18'), ('Gronkowski', '16'), ('Lewis', '16')], 'ReceivingYds': [('Amendola', '348'), ('Jeffery', '219'), ('Gronkowski', '218'), ('Thomas', '216'), ('Diggs', '207')], 'ReceivingAvg': [('Burkhead', '45.0'), ('Bryant', '39.0'), ('Cole', '27.3'), ('Dorsett', '25.0'), ('Watkins', '23.0')], 'ReceivingTD': [('Gronkowski', '3'), ('Jeffery', '3'), ('Amendola', '2'), ('Brown', '2'), ('Davis', '2')], 'ReceivingLng': [('Ginn', '80'), ('Diggs', '61'), ('McCaffrey', '56'), ('Clement', '55'), ('Jeffery', '53')], 'Receiving1stDowns': [('Amendola', '17'), ('Gronkowski', '15'), ('Ertz', '12'), ('Jones', '12'), ('Thomas', '12')], 'Receiving20+': [('Amendola', '6'), ('Gronkowski', '4'), ('Jeffery', '4'), ('Brown', '3'), ('Decker', '3')], 'Receiving40+': [('Agholor', '1'), ('Amendola', '1'), ('Brown', '1'), ('Bryant', '1'), ('Burkhead', '1')], 'ReceivingFumbles': [('Abbrederis', '0'), ('Abdullah', '0'), ('Adams', '0'), ('Adams', '0'), ('Adams', '0')], 'TackleTotal': [('Smith', '24'), ('Chung', '21'), ('Jack', '19'), ('Darby', '18'), ('Bell', '17')], 'Sacks': [('Butler', '2.0'), ('Dareus', '2.0'), ('Fowler Jr.', '2.0'), ('Grissom', '2.0'), ('McKinley', '2.0')], 'Interceptions': [('Adams', '1'), ('Barr', '1'), ('Colvin', '1'), ('Graham', '1'), ('Harmon', '1')]}
        self.data_list = [' PassingAtt ', 'Brady   139 ', 'Foles   106 ', 'Keenum  88  ', 'Bortles 85  ', 'Brees   73  ', 'PassingComp ', 'Brady   89  ', 'Foles   77  ', 'Keenum  53  ', 'Bortles 49  ', 'Brees   48  ', ' PassingPct ', 'Burton  100.0', 'Smith   72.7', 'Foles   72.6', 'Brees   65.8', 'Ryan    65.2', ' PassingYds ', 'Brady   1132', 'Foles   971 ', 'Brees   670 ', 'Bortles 594 ', 'Keenum  589 ', ' PassingAvg ', 'Amendol 10.0', 'Brees   9.2 ', 'Foles   9.2 ', 'Newton  8.7 ', 'Brady   8.1 ', 'PassingYards/Att', 'Amendol 10.0', 'Brees   9.2 ', 'Foles   9.2 ', 'Newton  8.7 ', 'Brady   8.1 ', ' PassingTD  ', 'Brady   8   ', 'Foles   6   ', 'Brees   5   ', 'Roethli 5   ', 'Mariota 4   ', ' PassingTD% ', 'Burton  100.0', 'Roethli 8.6 ', 'Brees   6.8 ', 'Smith   6.1 ', 'Mariota 5.9 ', ' PassingInt ', 'Brees   3   ', 'Keenum  3   ', 'Foles   1   ', 'Mariota 1   ', 'Peterma 1   ', 'PassingInt% ', 'Peterma 33.3', 'Brees   4.1 ', 'Keenum  3.4 ', 'Taylor  2.7 ', 'Roethli 1.7 ', ' PassingLng ', 'Brees   80  ', 'Keenum  61  ', 'Newton  56  ', 'Foles   55  ', 'Ryan    52  ', ' Passing20+ ', 'Brady   18  ', 'Foles   12  ', 'Bortles 10  ', 'Keenum  8   ', 'Brees   7   ', ' Passing40+ ', 'Foles   4   ', 'Brady   3   ', 'Bortles 2   ', 'Brees   2   ', 'Roethli 2   ', 'PassingSacks', 'Mariota 11  ', 'Ryan    6   ', 'Brady   4   ', 'Newton  4   ', 'Smith   4   ', 'PassingSackY', 'Mariota 69  ', 'Roethli 59  ', 'Newton  43  ', 'Ryan    35  ', 'Brees   23  ', 'PassingQBRating', 'Burton  118.8', 'Smith   116.2', 'Foles   115.7', 'Roethli 110.5', 'Brady   108.6', ' RushingAtt ', 'Fournet 70  ', 'Ajayi   42  ', 'Henry   35  ', 'Lewis   33  ', 'Blount  29  ', ' RushingYds ', 'Fournet 242 ', 'Ajayi   184 ', 'Henry   184 ', 'Lewis   135 ', 'Blount  130 ', ' RushingAvg ', 'Hill    14.0', 'Jones   13.0', 'Ginn    11.0', 'Thompso 9.0 ', 'Roethli 8.0 ', ' RushingTD  ', 'Fournet 4   ', 'Blount  3   ', 'White   3   ', 'Bolden  1   ', 'Freeman 1   ', ' RushingLng ', 'Blount  36  ', 'Henry   35  ', 'Gurley  33  ', 'Stewart 29  ', 'Ajayi   26  ', 'Rushing1stDowns', 'Fournet 15  ', 'Ajayi   8   ', 'Blount  8   ', 'Coleman 8   ', 'Henry   6   ', 'Rushing1stDowns%', 'Ginn    100.0', 'Ham     100.0', 'Hill    100.0', 'Jones   100.0', 'Line    100.0', ' Rushing20+ ', 'Bell    2   ', 'Blount  2   ', 'Gurley  2   ', 'Henry   2   ', 'Agholor 1   ', ' Rushing40+ ', 'Abbrede 0   ', 'Abdulla 0   ', 'Adams   0   ', 'Adams   0   ', 'Adams   0   ', ' RushingFum ', 'Ajayi   1   ', 'Bortles 1   ', 'Foles   1   ', 'Henry   1   ', 'Peterma 1   ', 'ReceivingTgt', 'Amendol 33  ', 'Gronkow 27  ', 'Jones   26  ', 'Diggs   22  ', 'Ertz    22  ', 'ReceivingRec', 'Amendol 26  ', 'Ertz    18  ', 'Jones   18  ', 'Gronkow 16  ', 'Lewis   16  ', 'ReceivingYds', 'Amendol 348 ', 'Jeffery 219 ', 'Gronkow 218 ', 'Thomas  216 ', 'Diggs   207 ', 'ReceivingAvg', 'Burkhea 45.0', 'Bryant  39.0', 'Cole    27.3', 'Dorsett 25.0', 'Watkins 23.0', 'ReceivingTD ', 'Gronkow 3   ', 'Jeffery 3   ', 'Amendol 2   ', 'Brown   2   ', 'Davis   2   ', 'ReceivingLng', 'Ginn    80  ', 'Diggs   61  ', 'McCaffr 56  ', 'Clement 55  ', 'Jeffery 53  ', 'Receiving1stDowns', 'Amendol 17  ', 'Gronkow 15  ', 'Ertz    12  ', 'Jones   12  ', 'Thomas  12  ', 'Receiving20+', 'Amendol 6   ', 'Gronkow 4   ', 'Jeffery 4   ', 'Brown   3   ', 'Decker  3   ', 'Receiving40+', 'Agholor 1   ', 'Amendol 1   ', 'Brown   1   ', 'Bryant  1   ', 'Burkhea 1   ', 'ReceivingFumbles', 'Abbrede 0   ', 'Abdulla 0   ', 'Adams   0   ', 'Adams   0   ', 'Adams   0   ', 'TackleTotal ', 'Smith   24  ', 'Chung   21  ', 'Jack    19  ', 'Darby   18  ', 'Bell    17  ', '   Sacks    ', 'Butler  2.0 ', 'Dareus  2.0 ', 'Fowler  2.0 ', 'Grissom 2.0 ', 'McKinle 2.0 ', 'Interceptions', 'Adams   1   ', 'Barr    1   ', 'Colvin  1   ', 'Graham  1   ', 'Harmon  1   ']

    def test_get_stats(self):
        stats = self.data.get_stat_list()
        self.assertIs(True)

    def test_dict_to_list(self):
        self.assertTrue(self.data.dict_to_list(self.stat_dict))

    def test_list_to_string(self):
        self.assertTrue(self.data.list_to_string(self.data_list))


