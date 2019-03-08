import re
import struct


comma = ord(',')
typeint = ord('i')
typefloat = ord('f')
typestring = ord('s')


# TODO: veryfing recursion opportunity
def add_null(cs):
    if len(cs) % 4 == 0:
        return cs
    else:
        cs.append(0)
        return add_null(cs)


"""def add_null(cs):
    le = 4 - (len(cs) % 4)
    if le != 4:
        for _ in range(le):
            cs.append(0)
    return cs"""


def int_to_bytes(n):
    conv = struct.pack('>i', n)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def float_to_bytes(f):
    conv = struct.pack('>f', f)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def string_to_bytes(s):
    conv = [ord(c) for c in s]
    conv.append(0)
    return add_null(conv)


def parse_msg(*msg):
    types = [comma]
    message = []
    for i in msg:
        if type(i) == int:
            types.append(typeint)
            message = message + int_to_bytes(i)
        elif type(i) == float:
            types.append(typefloat)
            message = message + float_to_bytes(i)
        elif type(i) == str:
            types.append(typestring)
            message = message + string_to_bytes(i)
    types.append(0)
    return add_null(types) + message


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


def parse_msgcontent(*msg):
    pass


def parse_mess(address, *msg):
    address_bytes = parse_address(address)
    types = parse_msg(*msg)
    return address_bytes + types

    # messaggio =
print(parse_mess('/ciaociao', 1, 2, 3))
