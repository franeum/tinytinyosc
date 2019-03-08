import re


def parse_msg(msg):
    pass


def parse_address(st):
    try:
        pattern = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
        if re.search(pattern, st):
            return 1
        else:
            return 0
    except TypeError as e:
        return e


print(parse_begin(10))
