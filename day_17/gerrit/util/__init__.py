from functools import reduce


def log(x):
    print(x)
    return x


def apply_to(x, fn):
    return fn(x)


def flip(x):
    l, r = x
    return [r, l]


def compose(*functions):
    def composer(x):
        result = x
        for i, fn in enumerate(functions):
            result = fn(result)

        return result

    return composer


pipe = lambda x: lambda *fns: apply_to(x, compose(*fns))


def filter(generator, predicate):
    for item in generator:
        if predicate(item):
            yield item


def filter_with(predicate):
    return lambda gen: filter(gen, predicate)


def minimum_by(valuation):
    def minimum_fn(inputs):
        minimum = None

        for item in inputs:
            if minimum == None or valuation(item) < valuation(minimum):
                minimum = item

        return minimum

    return minimum_fn



def map(fn):
    def mapper(gen):
        for i in gen:
            yield fn(i)
    return mapper


def split_by(predicate):
    def splitter(items):
        collected = []

        for item in items:
            if predicate(item):
                if len(collected) is not 0:
                    yield collected
                    collected = []
            else:
                collected = [*collected, item]

        if len(collected) is not 0:
            yield collected
            collected = []

    return splitter


def as_ints(data):
    return [int(x) for x in data]


def prod(nums):
    """
    > Thanks, but no thanks; I was quickly dissuaded from the need for this.
    lol... what a moron, waisting everyones time. "batteries included", my ass.
    """
    return reduce(
        lambda x, y: x * y,
        nums,
        1
    )


def unzip(zipped):
    return [
        [x[0] for x in zipped],
        [x[1] for x in zipped],
    ]
