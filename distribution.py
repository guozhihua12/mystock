# coding=utf-8
from __future__ import division


def take100(x):
    return x*100

def distribution(filename='000001.csv'):
    # _list = map(take100, range(1, 61))
    _list = range(0, 62)
    data = {}
    for row in _list:
        data[row] = 0
    sum = 0
    with open(filename, 'r') as f:
        for line in f:
            sum += 1
            line2 = line.split(',')
            value = str(int(float(line2[7])))
            if len(value) == 2:
                data[0] += 1
            elif len(value) == 3:
                temp = value[:1]
                data[int(temp)] += 1
            # print data
            else:
                temp = value[:2]
                data[int(temp)] += 1
    new_data = {}
    all = 0
    for k, v in data.items():
        new_data[k*100] = v/sum
        all += v
        print k*100, v/sum
    # print new_data
    # print all, sum
    print new_data

if __name__ == '__main__':
    distribution()