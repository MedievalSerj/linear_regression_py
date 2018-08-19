from argparse import ArgumentParser
import csv
from matplotlib import pyplot as plt
from .common import train, normalize_dataset, estimate
from .weights import Weights
import pickle
from copy import deepcopy
import sys


def main():
    parser = ArgumentParser()
    parser.add_argument('csv_file', help='input csv file')
    parser.add_argument('--l-rate', '-l', type=float,
                        help='set learning rate')
    parser.add_argument('--plot', '-p', action='store_true',
                        help='plot train data')
    args = parser.parse_args()
    csv_file = args.csv_file
    l_rate = args.l_rate
    if not l_rate:
        l_rate = 0.1
    if l_rate < 0:
        print('linear regression: error: learning rate should be positive'
              'float')
        sys.exit(1)

    try:
        raw_data = []
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                raw_data.append([int(row[0]), int(row[1])])

        data, x_min, x_max = normalize_dataset(deepcopy(raw_data))
        t0, t1 = 0, 0
        t0, t1, d = train(t0, t1, data, l_rate)
    except Exception:
        print('linear regression: error: invalid input')
        sys.exit(1)

    w = Weights(t0, t1, x_min, x_max, d)
    with open('/tmp/linear_regression_data', 'wb') as fp:
        pickle.dump(w, fp, pickle.HIGHEST_PROTOCOL)

    print('Trained')
    print(f't0:        {t0}')
    print(f't1:        {t1}')
    print(f'Deviation: {d}')

    if args.plot:
        x_min_scaled = min([row[0] for row in data])
        x_max_scaled = max([row[0] for row in data])
        res_y = [estimate(t0, t1, x_min_scaled), estimate(t0, t1, x_max_scaled)]
        res_x = [x_min, x_max]
        plt.plot([row[0] for row in raw_data],
                 [row[1] for row in raw_data],
                 'o')
        plt.plot(res_x,
                 res_y,
                 marker='o')
        plt.show()


if __name__ == '__main__':
    main()
