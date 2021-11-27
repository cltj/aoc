from aocd import get_data


def lines(*args, **kwargs):
    string = get_data(*args, **kwargs)
    return string.splitlines()


def numbers(*args, **kwargs):
    return [int(line) for line in lines(*args, **kwargs)]
