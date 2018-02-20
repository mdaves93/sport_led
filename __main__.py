import sys

import sports_feeds.get_data
import sports_feeds.parse_data
import led_sign.send_to_sign
import time

if __name__ == '__main__':
    while True:
        feed = sports_feeds.get_data.GetNhl()
        data = sports_feeds.parse_data.FeedData(feed.get_current_scores())
        send = led_sign.send_to_sign.SendToSign()
        send.send_to_sign(data.simplify_list())
        time.sleep(300)
