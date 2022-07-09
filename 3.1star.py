import functools
from redis import StrictRedis

redis_dict = StrictRedis(host='localhost', port=6379, db=0)


def cached(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if redis_dict.exists(str(args[0])) == 0:
            result = func(*args, **kwargs)
            redis_dict.set(str(args[0]), str(result))
            return result
        else:
            return int(redis_dict.get((args[0])))

    return wrapper


@cached
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(multiplier(7))
    print(multiplier(7))
    print(multiplier(8))
    print(multiplier(8))

