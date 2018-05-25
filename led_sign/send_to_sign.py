from pyledsign.minisign import MiniSign
import logging
import unidecode
from time import sleep


class SendToSign:

    def __init__(self):
        self.sign = MiniSign(devicetype='sign')
        self.logger = logging.getLogger()

    def queue_data(self, string_data):
        self.sign = MiniSign(devicetype='sign')
        new_string = unidecode.unidecode(string_data)
        if len(new_string) < 256:
            self.sign.queuemsg(data=new_string, speed=1, effect='hold')
        else:
            length = len(new_string)
            start = 0
            end = 252
            for i in range(1, 9):
                if end > length:
                    self.sign.queuemsg(data=new_string[start:length], speed=1, effect='hold')
                    break
                self.sign.queuemsg(data=new_string[start:end], speed=1, effect='hold')
                start += 252
                end += 252

        self.logger.info(new_string)

    def send_data(self):
        self.sign.sendqueue(device='/dev/ttyUSB0')
