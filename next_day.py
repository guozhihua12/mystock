# coding=utf-8
from __future__ import division


# 计算，今天跌，明天涨
def down_up_day(filename='000001.csv'):
    old_data = 0
    sum = 0
    down = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(old_data)> 0 > float(line2[9]):
                down += 1
                # print line2[0]
            old_data = line2[9]
    print 'down up: %.5f' % (float(down/sum))


# 连续涨两天的概率
def two_day_up(filename='000001.csv'):
    old_data = 0
    sum = 0
    up = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) > 0 and float(old_data) > 0:
                up += 1
                # print line2[0]
            old_data = line2[9]
    print 'up up: %.5f' % (float(up/sum))


# 连续涨三天的概率
def three_day_up(filename='000001.csv'):
    old_data = 0
    old_data2 = 0
    sum = 0
    up = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) > 0 and float(old_data) > 0 and float(old_data2) > 0:
                up += 1
                # print line2[0]
            old_data, old_data2 = line2[9], old_data
    print 'up up up: %.5f' % (float(up/sum))


# 连续涨四天的概率
def four_day_up(filename='000001.csv'):
    old_data = 0
    old_data2 = 0
    old_data3 = 0
    sum = 0
    up = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) > 0 and float(old_data) > 0 and float(old_data2) > 0 and float(old_data3) > 0:
                up += 1
                # print line2[0]
            old_data, old_data2, old_data3 = line2[9], old_data, old_data2
    print 'up up up up: %.5f' % (float(up/sum))

# 计算，今天涨，明天跌
def up_down_day(filename='000001.csv'):
    old_data = 0
    sum = 0
    up = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) > 0 > float(old_data):
                up += 1
                # print line2[0]
            old_data = line2[9]
    print 'up down: %.5f' % (float(up/sum))

# 连续跌两天的概率
def two_day_down(filename='000001.csv'):
    old_data = 0
    sum = 0
    down = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) < 0 and float(old_data) < 0:
                down += 1
                # print line2[0]
            old_data = line2[9]
    print 'down down: %.5f' % (float(down/sum))

# 连续跌三天的概率
def three_day_down(filename='000001.csv'):
    old_data = 0
    old_data2 = 0
    sum = 0
    down = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) < 0 and float(old_data) < 0 and float(old_data2) < 0:
                down += 1
                # print line2[0]
            old_data, old_data2 = line2[9], old_data
    print 'down down down: %.5f' % (float(down/sum))

# 连续跌三天的概率
def four_day_down(filename='000001.csv'):
    old_data = 0
    old_data2 = 0
    old_data3 = 0
    sum = 0
    down = 0
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.split(',')
            sum += 1
            if float(line2[9]) < 0 and float(old_data) < 0 and float(old_data2) < 0 and float(old_data3) < 0:
                down += 1
                # print line2[0]
            old_data, old_data2, old_data3 = line2[9], old_data, old_data2
    print 'down down down down: %.5f' % (float(down/sum))

if __name__ == '__main__':
    down_up_day()
    two_day_up()
    three_day_up()
    four_day_up()

    up_down_day()
    two_day_down()
    three_day_down()
    four_day_down()
