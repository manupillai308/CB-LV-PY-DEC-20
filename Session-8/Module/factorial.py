def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


def sum(n):

    if isinstance(n, list):
        return -1

    if n == 0:
        return 0
    return n + sum(n-1)

_x = 10
def _module_function():
    print("I'm a module function")
# def random():
#     pass
