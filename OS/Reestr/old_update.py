import os
import datetime
import list_ban
import requests
from fake_useragent import UserAgent


def isOld():
    files = os.listdir()

    timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
    for file in files:
        if file.endswith('.json'):
            file_name = file[:-5]
            try:
                if timestamp - int(file_name) < 60 * 60 * 3:
                    return file
                else:
                    os.remove(file)
            except Exception:
                continue
    return ''


def update():
    filename = isOld()
    if len(filename) == 0:
        print('Downloading new banList, please wait...')
        timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
        url = list_ban.list_ban
        ua = UserAgent()
        headers = {}
        headers['User-Agent'] = ua.chrome
        banList = requests.get(url, headers=headers)
        filename = '%s.json' % timestamp
        f = open(filename, 'wb')
        f.write(banList.content)
        f.close()
        print('Downloaded!')
        return filename
    else:
        print('banList version is OK!')
        return filename
