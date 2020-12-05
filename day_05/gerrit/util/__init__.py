def pipe(x):
    def piper(*functions):
        result = x
        for fn in functions:
            result = fn(x)

        return result

    return piper


def filter(generator, predicate):
    for item in generator:
        if predicate(item):
            yield item


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
