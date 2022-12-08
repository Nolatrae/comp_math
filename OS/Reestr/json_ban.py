import json

import old_update


class banList:
    IPs = []
    date = ''
    domain = ''
    URL = ''
    oder = ''
    issuedBy = ''

    def __init__(self, IPs, date, domain, URL, order, issuedBy):
        self.IPs = IPs
        self.date = date
        self.domain = domain
        self.URL = URL
        self.order = order
        self.issuedBy = issuedBy

    def __str__(self):
        output = "URL %s was banned %s.\nDomain: %s.\nIPs: %s.\n" \
                 "By %s. Order: %s." % (self.URL, self.date, self.domain, self.IPs, self.issuedBy, self.order)
        return output

    def isIPBanned(self, IP):
        if IP in self.IPs:
            return True
        return False

    def isURLBanned(self, URL):
        if URL[-1] == '/':
            URL = URL[:-1]
        if self.URL == URL:
            return True
        return False

    def isDomainBanned(self, domain):
        if self.domain == domain:
            return True
        return False


class banListArray:
    banList = []

    def isIPBanned(self, IP):
        for position in self.banList:
            if position.isIPBanned(IP):
                return position
        return None

    def isURLBanned(self, URL):
        for position in self.banList:
            if position.isURLBanned(URL):
                return position
        return None

    def isDomainBanned(self, domain):
        for position in self.banList:
            if position.isDomainBanned(domain):
                return position
        return None

    def __init__(self, filename):
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
        dateKey = list(data.keys())[0]
        jsonData = data[dateKey]
        for jsonPostion in jsonData:
            IPs = jsonPostion['ip']
            date = jsonPostion['date']
            domain = jsonPostion['page']
            URL = jsonPostion['link']
            order = jsonPostion['postanovlenie']
            issuedBy = jsonPostion['gos_organ']
            banListPostion = banList(IPs, date, domain, URL, order, issuedBy)
            self.banList.append(banListPostion)


def getbanList():
    filename = old_update.update()
    print('banList filename is %s' % filename)
    return banListArray(filename)
