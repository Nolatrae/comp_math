def strIpToInt32(ip):
    ipParts = list(map(int, ip.split('.')))
    return ipParts[3] + ipParts[2] * (1 << 8) + ipParts[1] * (1 << 16) + ipParts[0] * (1 << 24)


class SubNet:
    ip = ''
    subNetSize = 0
    subNet32 = 0

    def __init__(self, ip, subNetSize):
        super().__init__()
        self.ip = ip
        self.subNetSize = subNetSize
        self.subNet32 = ((strIpToInt32(ip) >> (32 - subNetSize)) << (32 - subNetSize))

    def isIpInSubnet(self, ip):
        ip32 = strIpToInt32(ip)
        if ip32 - self.subNet32 < (1 << (32 - self.subNetSize)) and ip32 - self.subNet32 > 0:
            return True
        else:
            False
