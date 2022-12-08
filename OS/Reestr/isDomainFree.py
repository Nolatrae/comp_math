import re
import whois
from threading import Thread
import json_ban as jb

TOTAL = 0


def scan(begin, end, domain_list, th_id):
    open('./output/freeDomains' + str(th_id) + '.txt', 'w').close()
    for i in range(begin, end):
        domain = domain_list[i]
        global TOTAL
        TOTAL += 1
        print(TOTAL, '/', len(domain_list), 'thread: ', th_id, 'domain_no: ', i)
        try:
            whoidData = whois.whois(domain)
            print('Domain STATUS: ', whoidData.status)
            if whoidData.status is None:
                print('FREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
                f = open('./output/freeDomains' + str(th_id) + '.txt', 'a')
                f.write(domain + '\n')
                f.close()
        except Exception as e:
            print(e)
            continue


blackList = jb.getbanList()

unicDomains = set()


for item in blackList.banList:
    URL = item.URL
    try:
        domain = re.search(r'https?://([A-Za-z_0-9.-]+).*', URL).group(1)
        unicDomains.add(domain)
    except Exception:
        continue

domain_list = list(unicDomains)

n = 16

for i in range(n):
    th = Thread(target=scan, args=(i*len(domain_list)//n, (i+1)*len(domain_list)//n, domain_list, i, ))
    th.start()

#f.close()
