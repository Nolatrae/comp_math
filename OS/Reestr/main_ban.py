import re
import socket
import json_ban
BanList = json_ban.getbanList()


while True:
    print('\n Enter URL to check it in BanList: ')
    URL = input()

    print('1. Check ban by URL...')
    urlBanned = BanList.isURLBanned(URL)
    if urlBanned is None:
        print('URL is no banned..')
    else:
        print(urlBanned)
    print('______________________________\n')


    domen = re.search(r'https?://([A-Za-z_0-9.-]+).*', URL).group(1)
    print('2. Check by domen: ', domen)
    domenBan = BanList.isDomainBanned(domen)
    if domenBan is None:
        print('domen is not banned!')
    else:
        print(domenBan)
    print('______________________________\n')

    ip = socket.gethostbyname(domen)
    print('3. Checking by IP:', ip)
    ipBan = BanList.isIPBanned(ip)
    if ipBan is None:
        print('IP is not banned')
    else:
        print(ipBan)
    print('______________________________\n\n')