# coding=utf-8
from __future__ import division
from datetime import date, datetime
import time


__author__ = 'apple'


def main(filename='000001.csv'):
    # 最高值
    high = 0
    # high_time = 0
    # # 最低值
    # low = 0
    # low_time = 0
    # # 涨幅最大
    # gains = 0
    # gains_time = 0
    # # 跌幅最大
    # drop = 0
    # drop_time = 0
    # # 最大成交额
    # high_turnover = 0
    # high_turnover_time = 0
    # # 最小成交额
    # low_turnover = 0
    # low_turnover_time = 0

    with open(filename, 'r') as f:
        for line in f:
            # print line
            try:

                line2 = line.split(',')
            # print float(line2[9]), type(float(line2[9]))
            # print line2[0], line2[1]
            # print line2[0], line2[1], line2[2], line2[3], line2[4], line2[5], line2[6], line2[7], line2[8], line2[9], line2[10], line2[11]
    #         print line2[7]
                if not high:
                    high = float(line2[7])
                    high_time = line2[0]
                    low = float(line2[7])
                    low_time = line2[0]
                    gains = float(line2[9])
                    gains_time = line2[0]
                    drop = float(line2[9])
                    drop_time = line2[0]
                    high_turnover = float(line2[11])
                    high_turnover_time = line2[0]
                    low_turnover = float(line2[11])
                    low_turnover_time = line2[0]
                if float(line2[7]) > high:
                    high = float(line2[7])
                    high_time = line2[0]
                if float(line2[7]) < low:
                    low = float(line2[7])
                    low_time = line2[0]

                if line2[9] and float(line2[9]) > gains:
                    gains = float(line2[9])
                    gains_time = line2[0]
                if line2[9] and float(line2[9]) < drop:
                    drop = float(line2[9])
                    drop_time = line2[0]

                if float(line2[11]) > high_turnover:
                    high_turnover = float(line2[11])
                    high_turnover_time = line2[0]
                if float(line2[11]) < low_turnover:
                    low_turnover = float(line2[11])
                    low_turnover_time = line2[0]
            except:
                pass
    #
    print 'high: %s time: %s' % (high, high_time)
    print 'low: %s time: %s' % (low, low_time)
    print 'gains: %s time: %s' % (gains, gains_time)
    print 'drop: %s time: %s' % (drop, drop_time)
    print 'high_turnover: %s time: %s' % (high_turnover, high_turnover_time)
    print 'low_turnover: %s time: %s' % (low_turnover, low_turnover_time)


if __name__ == '__main__':
    main()
