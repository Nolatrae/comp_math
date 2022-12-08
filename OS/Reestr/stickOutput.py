import os


def stick():
    dir = './output'
    domains = ''
    files = os.listdir(dir)
    for file in files:
        f = open(dir + '/' + file, 'r')
        data = f.read()
        domains+=data
        f.close()
    f = open('output.txt', 'w')
    f.write(domains)
    f.close()

if __name__ == '__main__':
    stick()