from operator import attrgetter


def get(iterable, **kwargs: dict):
    """Find an element of ``iterable`` with the attributes
    specified in kwargs. For example:

        get(assignments, id='an id here') # >>> <Assignment...>

    Also supports nested attributes:

        # Get assignments that last 100 minutes
        get(assignments, due_by__total_seconds=100*60)

    Parameters
    ----------
    iterable : any
        An iterable to search through
    """
    if len(kwargs) == 1:
        # Most common use case
        k, v = kwargs.popitem()
        pred = attrgetter(k.replace("__", "."))
        for element in iterable:
            if pred(element) == v:
                return element
    else:
        # More complicated use case
        # Convert nested attributes to dotted attributes
        converted = [
            (attrgetter(kwarg.replace("__", ".")), value)
            for kwarg, value in kwargs.items()
        ]

        for element in iterable:
            if all(pred2(element) == value for pred2, value in converted):
                return element

    # Oops, nothing was found :c
    return None


def get_all(iterable, **kwargs: dict):
    """Like :func:`get`, but to get all instances, not just the first.

    Parameters
    ----------
    iterable : any
        An iterable to search through
    """
    results = []
    copy = iterable[:]
    current = get(copy, **kwargs)
    while current is not None:
        copy.remove(current)
        results.append(current)
        current = get(copy, **kwargs)

    return results
