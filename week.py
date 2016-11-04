# coding=utf-8
from __future__ import division
from datetime import date, datetime
import time
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# print sys.getdefaultencoding()

__author__ = 'apple'

week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }


def get_week_day(date):
    day = date.weekday()
    return week_day_dict[day]


def traverse_all_data(filename='000001.csv'):
    weeks = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    sum = 0
    with open(filename, 'r') as f:
        for line in f:
            # print line
            line2 = line.split(',')
            temp_time = time.strptime(line2[0], "%Y-%m-%d")
            temp_date = datetime(* temp_time[:6])
            sum += 1
            if line2[9][0] != '-':
                weeks[temp_date.weekday()] += 1
    # print weeks
    # print sum
    #
    #     weeks[(week_day_dict[k])] = v/(sum/5)
    #     weeks.pop(k)
    # print weeks

    filename = 'all_weeks_test.txt'
    with open(filename, 'w') as f:
        for k, v in weeks.items():
            line = '%s %s\n' % (week_day_dict[k], v/(sum/5))
            f.write(line)

if __name__ == '__main__':
    # day = date.today()
    traverse_all_data()