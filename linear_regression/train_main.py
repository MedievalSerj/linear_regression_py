from argparse import ArgumentParser
import csv
from matplotlib import pyplot


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('csv_file', help='input csv file')
    args = parser.parse_args()
    csv_file = args.csv_file
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append([int(row[0]), int(row[1])])

    pyplot.plot([row[0] for row in data],
                [row[1] for row in data],
                'ro')
    pyplot.show()
