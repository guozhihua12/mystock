# coding=utf-8

# __author__ = 'apple'
from today import sync
from datetime import date, timedelta


def main():
    # day = date.today().strftime('%m-%d')
    day = date.today()
    # 计算未来一个月
    data = []
    for i in range(31):
        temp = (day + timedelta(days=i))
        data.append([temp.strftime('%Y-%m-%d'), sync(temp.strftime('%m-%d'))])
    filename = '%s-%s.txt' % (day.strftime('%Y%m%d'), temp.strftime('%Y%m%d'))
    with open(filename, 'w') as f:
        for row in data:
            # print row, type(row)
            line = '%s %s\n' % (row[0], row[1])
            f.write(line)


if __name__ == '__main__':
    main()
