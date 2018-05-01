class Changer:

    @staticmethod
    def dict_to_list(stat_dict):
        stat_list = []
        for stat in stat_dict:
            stat_list.append("{:^12}".format(str(stat)))
            for player in stat_dict[stat]:
                stat_list.append("{:7s} {:4s}".format(player[0][:7], player[1][:4]))
        return stat_list

    @staticmethod
    def list_to_string(list_data):
        string = "".join(data for data in list_data)
        return string
