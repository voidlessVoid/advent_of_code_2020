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


def filter(generator, predicate):
    for item in generator:
        if predicate(item):
            yield item


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
