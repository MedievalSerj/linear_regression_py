from argparse import ArgumentParser
import csv
from matplotlib import pyplot
from .common import train


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('csv_file', help='input csv file')
    parser.add_argument('--l-rate', '-l', type=float,
                        help='set learning rate')
    args = parser.parse_args()
    csv_file = args.csv_file
    l_rate = args.l_rate

    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append([int(row[0]), int(row[1])])

    pyplot.plot([row[0] for row in data],
                [row[1] for row in data],
                'ro')
    # pyplot.show()
    t0, t1 = 0, 0
    t0, t1 = train(t0, t1, data, l_rate)
    print('Solved')
    print(f't0={t0}')
    print(f't1={t1}')
