from math import sqrt


def estimate(t0, t1, x):
    return t0 + t1 * x


def deviation(t0, t1, data):
    return sqrt(sum([(estimate(t0, t1, row[0]) - row[1]) ** 2
                     for row in data])
                / (len(data) - 1))


def make_step(t0, t1, data, l_rate):
    t0_tmp = 0
    t1_tmp = 0
    for row in data:
        t0_tmp += estimate(t0, t1, row[0]) - row[1]
        t1_tmp += ((estimate(t0, t1, row[0])) - row[1]) * row[0]
    t0 = t0 - (l_rate * t0_tmp) / len(data)
    t1 = t1 - (l_rate * t1_tmp) / len(data)
    return t0, t1


def train(t0, t1, data, l_rate=0.1):
    while True:
        t0_tmp, t1_tmp = make_step(t0, t1, data, l_rate)
        if t0_tmp == t0 and t1_tmp == t1:
            return t0, t1, deviation(t0, t1, data)
        else:
            t0, t1 = t0_tmp, t1_tmp


def normalize_dataset(data):
    x_max = max([row[0] for row in data])
    x_min = min([row[0] for row in data])
    for row in data:
        row[0] = (row[0] - x_min) / (x_max - x_min)
    return data, x_min, x_max


def normalize_x_value(x, x_max, x_min):
    return (x - x_min) / (x_max - x_min)
