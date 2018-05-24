class Changer:

    @staticmethod
    def dict_to_list(stat_dict, wanted_stats=("PassingYds", "PassingTD", "RushingYds", "RushingTD", "ReceivingYds",
                                              "ReceivingTD", "Interceptions", "TackleTotal", "Sacks" "BattingAvg",
                                              "HomeRuns", "RunsBattedIn", "Hits", "BatterSO", "BatterWalks", "StolenBases",
                                              "EarnedRunAvg", "Wins", "PitcherSO", "PitcherWalks", "Saves", "Pts",
                                              "Ast", "Stl", "Blk", "Reb", "Fg3PtMade", "Goals", "Assists", "Points",
                                              "HatTricks", "Shutouts")):
        stat_list = []
        for stat in stat_dict:
            if stat in wanted_stats:
                stat_list.append("{:^12s}".format(str(stat)[:12]))
                for player in stat_dict[stat]:
                    stat_list.append("{:7s} {:4s}".format(player[0][:7], player[1][:4]))
        return stat_list

    @staticmethod
    def list_to_string(list_data):
        string = "".join(data for data in list_data)
        return string
