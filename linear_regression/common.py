
def estimate_price(t0, t1, x):
    return t0 + t1 * x


def tmp_t0(t0, t1, data, l_rate):
    s = 0
    for row in data:
        s += estimate_price(t0, t1, row[0]) - row[1]
    return (l_rate / len(data)) * s


def tmp_t1(t0, t1, data, l_rate):
    s = 0
    for row in data:
        s += (estimate_price(t0, t1, row[0]) - row[1]) * row[0]
    return (l_rate / len(data)) * s


def train(t0, t1, data, l_rate):
    loss = loss_function(t0, t1, data)
    i = 0
    while True:
        t_0 = t0 - tmp_t0(t0, t1, data, l_rate)
        t1 = t1 - tmp_t1(t0, t1, data, l_rate)
        t0 = t_0
        loss_tmp = loss_function(t0, t1, data)
        if loss_tmp > loss:
            break
        else:
            loss = loss_tmp
        # print(f't0={t0}')
        # print(f't1={t1}')
        i += 1
        if i > 10:
            break
    return t0, t1


def loss_function(t0, t1, data):
    s = 0
    for row in data:
        s += (estimate_price(t0, t1, row[0]) - row[1]) ** 2
    return s / (2 * len(data))
