import re
import struct


COMMA = ord(',')
TYPE_INT = ord('i')
TYPE_FLOAT = ord('f')
TYPE_STRING = ord('s')


# TODO: verifying recursion opportunity
def add_null(cs):
    if len(cs) % 4 == 0:
        return cs
    else:
        cs.append(0)
        return add_null(cs)


# iterative version of the previous func
# see previous TODO
"""def add_null(cs):
    le = 4 - (len(cs) % 4)
    if le != 4:
        for _ in range(le):
            cs.append(0)
    return cs"""


def match_int(n):
    return type(n) == int


def int_to_bytes(n):
    conv = struct.pack('>i', n)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def match_float(n):
    return type(n) == float


def float_to_bytes(f):
    conv = struct.pack('>f', f)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def match_string(n):
    return type(n) == string


def string_to_bytes(s):
    conv = [ord(c) for c in s]
    conv.append(0)
    return add_null(conv)


parse_funx = ((match_int, int_to_bytes), (match_float, float_to_bytes),
              (match_string, string_to_bytes))

'''tps = (int, float, str)
tps_symbols = (TYPE_INT, TYPE_FLOAT, TYPE_STRING)
ass = [x for x in zip(tps, tps_symbols)]
print(ass)'''


def parse_msg(*msg):
    types = [COMMA]
    for atom in msg:
        for match, apply in parse_funx:
            if match(atom):
                print(apply)
                apply(atom)


'''def parse_msg(*msg):
    types = [COMMA]
    message = []
    for i in msg:
        if type(i) == int:
            types.append(TYPE_INT)
            message.extend(int_to_bytes(i))
        elif type(i) == float:
            types.append(TYPE_FLOAT)
            message.extend(float_to_bytes(i))
        elif type(i) == str:
            types.append(TYPE_STRING)
            message.extend(string_to_bytes(i))
    types.append(0)
    withnull_msg = add_null(types)
    withnull_msg.extend(message)
    return withnull_msg'''


def parse_address(st):
    try:
        address = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
        if re.search(address, st):
            return string_to_bytes(st)
        else:
            return '''address is not well formed, probably slash symbol (/)
            is not present or it's not in the right place'''
    except TypeError as e:
        return e


def parse_whole_mess(address, *msg):
    address_bytes = parse_address(address)
    types = parse_msg(*msg)
    return address_bytes + types
