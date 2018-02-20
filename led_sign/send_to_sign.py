from pyledsign.minisign import MiniSign


class SendToSign:

    def __init__(self):
        self.sign = MiniSign(devicetype='sign')

    def send_to_sign(self, data):
        for score in data:
            self.sign.queuemsg(data=score, speed=1, effect='hold')
        self.sign.sendqueue(device='/dev/ttyUSB0')
