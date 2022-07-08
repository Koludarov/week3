import functools


def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not cache.get(args):
            result = func(*args, **kwargs)
            cache[args] = result
            return result
        else:
            return cache[args]

    return wrapper


@cached
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(multiplier(2))
    print(multiplier(2))
