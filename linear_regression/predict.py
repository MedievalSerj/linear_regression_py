import pickle
import sys
from .common import estimate


def main():
    try:
        with open('/tmp/linear_regression_data', 'rb') as fp:
            w = pickle.load(fp)
            t0 = w.t0
            t1 = w.t1
            x_min = w.x_min
            x_max = w.x_max
            d = w.d
    except Exception:
        print('linear regression:'
              ' error: one should use "train" program first')
        sys.exit(1)
    print('Type "exit" to finish')
    while True:
        x = input('input millage: ')
        if type(x) == str and x == 'exit':
            sys.exit()
        try:
            x = float(x)
            x_norm = (x - x_min) / (x_max - x_min)
            est = estimate(t0, t1, x_norm)
            print(f'price={round(est, 2)} \u00B1 {round(d, 2)}')
        except Exception:
            print('error: not a valid float')


if __name__ == '__main__':
    main()
