import sports_feeds.get_data as get_data
from sports_feeds.format_data import FormatNflStats
from sports_feeds.format_data import FormatNhlStats
from sports_feeds.format_data import FormatMlbStats
from sports_feeds.format_data import FormatNbaStats
from sports_feeds.format_data import FormatScores
from sports_feeds.type_changer import Changer
from led_sign.send_to_sign import SendToSign

import time


class Main(object):

    def __init__(self, nhl_stats=None, nhl_scores=None,
                 nba_stats=None, nba_scores=None,
                 mlb_stats=None, mlb_scores=None,
                 nfl_stats=None, nfl_scores=None):
        if nhl_stats or nhl_scores:
            self.nhl_data = get_data.GetNhl(nhl_stats)
            self.get_nhl_scores = True
            self.get_nhl_stats = True
        else:
            self.get_nhl_scores = False
            self.get_nhl_stats = False
        self.nhl_scores = {}
        self.nhl_stats = {}

        if nba_stats or nba_scores:
            self.nba_data = get_data.GetNba(nba_stats)
            self.get_nba_scores = True
            self.get_nba_stats = True

        else:
            self.get_nba_scores = False
            self.get_nba_stats = False
        self.nba_scores = {}
        self.nba_stats = {}

        if mlb_stats or mlb_scores:
            if mlb_stats:
                mlb_stats = mlb_stats + ",IP"
            self.mlb_data = get_data.GetMlb(mlb_stats)
            self.get_mlb_scores = True
            self.get_mlb_stats = True
        else:
            self.get_mlb_scores = False
            self.get_mlb_stats = False
        self.mlb_scores = {}
        self.mlb_stats = {}

        if nfl_stats or nfl_scores:
            self.nfl_data = get_data.GetNfl(nfl_stats)
            self.get_nfl_scores = True
            self.get_nfl_stats = True
        else:
            self.get_nfl_scores = False
            self.get_nfl_stats = False
        self.nfl_scores = {}
        self.nfl_stats = {}

    def collect_scores(self):
        if self.get_nhl_scores:
            self.nhl_scores = FormatScores(self.nhl_data.get_current_scores()).format_score_list("NHL")
        if self.get_nba_scores:
            self.nba_scores = FormatScores(self.nba_data.get_current_scores()).format_score_list("NBA")
        if self.get_mlb_scores:
            self.mlb_scores = FormatScores(self.mlb_data.get_current_scores()).format_score_list("MLB")
        if self.get_nfl_scores:
            self.nfl_scores = FormatScores(self.nfl_data.get_current_scores()).format_score_list("NFL")

    def collect_stats(self):
        if self.get_nhl_stats:
            self.nhl_stats = FormatNhlStats(self.nhl_data.get_stats()).format_all_stats()
        if self.get_nba_stats:
            self.nba_stats = FormatNbaStats(self.nba_data.get_stats()).format_all_stats()
        if self.get_mlb_stats:
            self.mlb_stats = FormatMlbStats(self.mlb_data.get_stats()).format_all_stats()
        if self.get_nfl_stats:
            self.nfl_stats = FormatNflStats(self.nfl_data.get_stats()).format_all_stats()

    def collect_all(self):
        self.collect_scores()
        self.collect_stats()
        data = Changer.list_to_string(self.nhl_scores) + \
            Changer.list_to_string(Changer.dict_to_list(self.nhl_stats)) + \
            Changer.list_to_string(self.nba_scores) + \
            Changer.list_to_string(Changer.dict_to_list(self.nba_stats)) + \
            Changer.list_to_string(self.mlb_scores) + \
            Changer.list_to_string(Changer.dict_to_list(self.mlb_stats)) + \
            Changer.list_to_string(self.nfl_scores) + \
            Changer.list_to_string(Changer.dict_to_list(self.nfl_stats))
        return data


if __name__ == '__main__':
    while True:
        sign = SendToSign()
        # driver_class = Main("PTS", True, "3PM,STL", True, mlb_stats="SO,AVG,ERA", mlb_scores=True, "YDS", True)
        driver_class = Main(nfl_stats="YDS,TD", mlb_stats="SO,AVG,ERA", mlb_scores=True)
        data = driver_class.collect_all()
        print(data)
        sign.queue_data(data)
        sign.send_data()
        time.sleep(300)
