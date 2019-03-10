import re
import struct


COMMA = ord(',')
TYPE_INT = ord('i')
TYPE_FLOAT = ord('f')
TYPE_STRING = ord('s')


# TODO: verifying recursion opportunity
def append_null(cs):
    '''append null values at the end of a string'''

    if len(cs) % 4 == 0:
        return cs
    else:
        cs.append(0)
        return append_null(cs)


# iterative version of the previous func
# see previous TODO
"""def append_null(cs):
    le = 4 - (len(cs) % 4)
    if le != 4:
        for _ in range(le):
            cs.append(0)
    return cs"""


def match_int(n):
    return type(n) == int


def int_to_bytes(n):
    '''convert int to bytes (big endian)'''

    conv = struct.pack('>i', n)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def match_float(n):
    return type(n) == float


def float_to_bytes(f):
    '''convert float to bytes (big endian)'''

    conv = struct.pack('>f', f)
    conv = struct.unpack('>BBBB', conv)
    return list(conv)


def match_string(n):
    return type(n) == str


def string_to_bytes(s):
    '''convert string to bytes (big endian)'''

    conv = [ord(c) for c in s]
    conv.append(0)
    return append_null(conv)


parse_funx = ((match_int, int_to_bytes, TYPE_INT),
              (match_float, float_to_bytes, TYPE_FLOAT),
              (match_string, string_to_bytes, TYPE_STRING))


def parse_msg(*msg):
    '''parse message arguments and convert them in bytes'''

    types = [COMMA]
    message = []
    for atom in msg:
        for match, apply, byte_type in parse_funx:
            if match(atom):
                types.append(byte_type)
                message.extend(apply(atom))
    with_nulls_msg = append_null(types)
    with_nulls_msg.extend(message)
    return with_nulls_msg


def parse_address(st):
    '''parse address and convert it in bytes'''

    try:
        address = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
        if re.search(address, st):
            return string_to_bytes(st)
        else:
            return '''address is not well formed, probably slash symbol (/)
            is not present or it's not in the right place'''
    except TypeError as e:
        return e


def build_whole_mess(address, *msg):
    '''build whole message and prepare it to send'''

    address_bytes = parse_address(address)
    types = parse_msg(*msg)
    return address_bytes + types


class OSCClient:
    def __init__(self):
        pass

    def parse_msg(self, *msg):
        '''parse message arguments and convert them in bytes'''

        types = [COMMA]
        message = []
        for atom in msg:
            for match, apply, byte_type in parse_funx:
                if match(atom):
                    types.append(byte_type)
                    message.extend(apply(atom))
        with_nulls_msg = append_null(types)
        with_nulls_msg.extend(message)
        return with_nulls_msg

    def parse_address(self, st):
        '''parse address and convert it in bytes'''

        try:
            address = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
            if re.search(address, st):
                return string_to_bytes(st)
            else:
                return '''address is not well formed, probably slash symbol (/)
                is not present or it's not in the right place'''
        except TypeError as e:
            return e

    def build_whole_mess(self, address, *msg):
        '''build whole message and prepare it to send'''

        address_bytes = parse_address(address)
        types = parse_msg(*msg)
        return address_bytes + types


class Message:
    def __init__(self):
        pass

    def parse_msg(self, *msg):
        '''parse message arguments and convert them in bytes'''

        types = [COMMA]
        message = []
        for atom in msg:
            for match, apply, byte_type in parse_funx:
                if match(atom):
                    types.append(byte_type)
                    message.extend(apply(atom))
        with_nulls_msg = append_null(types)
        with_nulls_msg.extend(message)
        return with_nulls_msg

    def parse_address(self, st):
        '''parse address and convert it in bytes'''

        try:
            address = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
            if re.search(address, st):
                return string_to_bytes(st)
            else:
                return '''address is not well formed, probably slash symbol (/)
                is not present or it's not in the right place'''
        except TypeError as e:
            return e

    def build_whole_mess(self, address, *msg):
        '''build whole message and prepare it to send'''

        address_bytes = parse_address(address)
        types = parse_msg(*msg)
        return address_bytes + types
