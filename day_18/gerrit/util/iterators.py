def nats(start=0):
    n = start
    while True:
        yield n
        n = n + 1


def trajectory(operator):
    def trajectory_generator(inp):
        current = inp
        while True:
            yield current
            current = operator(current)

    return trajectory_generator


def assert_trajectory_correctness(operator, compare):
    def asserter(inp, requirements):
        for index, result in enumerate(trajectory(operator)(inp)):
            if index < len(requirements):
                compare(result, requirements[index])
            else:
                return

    return asserter


def trajectory_fixpoint(operator):
    THRESHOLD = 5000

    def stabilize_trajectory(inp):
        prev = inp

        for counter, nxt in enumerate(trajectory(operator)(inp)):
            if nxt == prev:
                return operator(nxt)
            if counter > THRESHOLD:
                return None

            prev = nxt

    return stabilize_trajectory


def take(n):
    def seq(iterator):
        for index, item in enumerate(iterator):
            if index < n:
                yield item
            else:
                return

    return seq


def get_nth(n, fallback=None):
    def getter(iterator):
        for index, item in enumerate(iterator):
            if index == n:
                return item

        return None

    return getter
