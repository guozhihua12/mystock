# coding=utf-8
from __future__ import division
from datetime import date


# 输入日期，查看历史的今日涨幅概率

def sync(day):
    filename = '000001.csv'
    sum = 0
    up = 0
    down = 0
    with open(filename, 'r') as f:
        for line in f:
            # print line
            line2 = line.split(',')
            # print line2[9]
            if line2[0][5:] == day:
                sum += 1
                if line2[9][0] == '-':
                    # print 'line2[9]<0'
                    # print line2[9]
                    down += 1
                else:
                    up += 1
    # print up, down, sum
    # print 'up rate:%.5f' % (float(up/sum))
    # print 'up rate:%.5f' % (float(up/sum))
    # print 'down rate:%.5f' % (float(down/sum))
    return float(up/sum)


if __name__ == '__main__':
    day = None
    # day = '11-03'
    if not day:
        day = date.today().strftime('%m-%d')
    sync(day)
