from pyledsign.minisign import MiniSign
import logging
from time import sleep


class SendToSign:

    def __init__(self):
        self.sign = MiniSign(devicetype='sign')
        self.logger = logging.getLogger()

    def queue_data(self, string_data):
        self.sign = MiniSign(devicetype='sign')
        print(self.sign.SLOTRANGE)
        if len(string_data) < 256:
            self.sign.queuemsg(data=string_data, speed=1, effect='hold')
        else:
            i = 1
            length = len(string_data)
            print(length)
            start = 0
            end = 252
            while True:
                if end > length:
                    self.sign.queuemsg(data=string_data[start:length], speed=1, effect='hold')
                    break
                self.sign.queuemsg(data=string_data[start:end], speed=1, effect='hold')
                start = end
                end = end * i
                i += 1
        self.logger.info(string_data)

    def send_data(self):
        self.sign.sendqueue(device='/dev/ttyUSB0')
