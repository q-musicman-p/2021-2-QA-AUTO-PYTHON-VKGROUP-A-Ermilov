import random
import time


def random_str(str_length=10, digits=True, use_time=True, alpha=True, spec_sym=False):

    if digits:
        current_time = str(time.time()) if use_time else ''
        if not spec_sym:
            current_time = current_time.replace('.', '')
        number = str(random.randint(0, 10**9)) + current_time
    else:
        number = ''

    string = ''.join(
        [chr(sym) for sym in [random.randint(65, 90) for _ in range(str_length)]] +
        [chr(sym) for sym in [random.randint(97, 122) for _ in range(str_length)]]
    ) if alpha else ''

    spec_sym = ''.join(
        [chr(sym) for sym in [random.randint(33, 64) for _ in range(str_length)]]
    ) if spec_sym else ''

    result = [sym for sym in (number + string + spec_sym)]
    random.shuffle(result)
    return ''.join(result)[:str_length]
