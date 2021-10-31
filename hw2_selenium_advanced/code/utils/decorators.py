import time


class TimeoutException(Exception):
    pass


def wait(method, error=Exception, waiting_time=None, interval=0.5, check=False, **kwargs):
    last_exception = None
    if waiting_time is None:
        waiting_time = 10

    started = time.time()
    while time.time() - started < waiting_time:
        try:
            result = method(**kwargs)
            if check:
                if result:
                    return result
                last_exception = f'Method {method.__name__} returned {result}'
            else:
                return result
        except error as e:
            last_exception = e

        time.sleep(interval)

    raise TimeoutException(f'Method {method.__name__} timeout out in {waiting_time}sec with exception: {last_exception}')