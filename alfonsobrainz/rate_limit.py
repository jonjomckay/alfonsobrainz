import threading
import time


def rate_limited(max_per_second=1.0):
    lock = threading.Lock()
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        def rate_limited_function(*args, **kargs):
            lock.acquire()

            elapsed = time.clock() - last_time_called[0]

            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            lock.release()

            ret = func(*args, **kargs)

            last_time_called[0] = time.clock()

            return ret

        return rate_limited_function

    return decorate