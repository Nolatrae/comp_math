def getMask(IPadres):
    mask = ''
    strIPadres = ['', '', '', '']
    byte = 3
    check = False
    for i in range(len(IPadres) - 1, -1, -1):
        if IPadres[i] == '/':
            check = True
            continue
        if check:
            if IPadres[i] == '.':
                byte -= 1
                continue
            strIPadres[byte] = IPadres[i] + strIPadres[byte]
        else:
            mask = IPadres[i] + mask
    IPadres = int(strIPadres[0]) * (2**24) + int(strIPadres[1]) * (2**16) + int(strIPadres[2]) * (2**8) + int(strIPadres[3])
    return int(mask), IPadres


def countByMask(IPadress):
    IPadressNum = 0
    for IPadres in IPadress:
        mask = getMask(IPadres)[0]
        IPadressNum += 2 ** (32 - mask)
    return IPadressNum

def countByIPadres(IPadress):
    IPadressList = set()
    for IPadres in IPadress:
        mask, IPadresInt = getMask(IPadres)
        startIPadres = (IPadresInt >> (32 - mask)) << (32 - mask)
        endIPadres = startIPadres + (2 ** (32 - mask) - 1)
        for i in range(startIPadres, endIPadres + 1):
            IPadressList.add(i)
    return len(IPadressList)

IPadress = []
f = open('blocked-networks.txt')
for line in f:
    IPadress.append(line)
f.close()

way1 = countByMask(IPadress)
way2 = countByIPadres(IPadress)

print(way1)
print(way2)
