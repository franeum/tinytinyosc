import parsemessage
import re


class OSCArgument:
    def __init__(self, *args):
        types = [parsemessage.COMMA]
        message = []
        for atom in args:
            for match, apply, byte_type in parsemessage.parse_funx:
                if match(atom):
                    types.append(byte_type)
                    message.extend(apply(atom))
        types.append(0)
        self.with_nulls_msg = parsemessage.append_null(types)
        self.with_nulls_msg.extend(message)

    def get_bytes_args(self):
        return self.with_nulls_msg


class OSCAddress:
    def __init__(self, addr):
        self.str_addr = addr

    def get_bytes_addr(self):
        try:
            address = '(^/{1}[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+)(/?[a-zA-Z0-9]+$)'
            if re.search(address, self.str_addr):
                return parsemessage.string_to_bytes(self.str_addr)
            else:
                return '''address is not well formed, probably slash symbol (/)
                is not present or it's not in the right place'''
        except TypeError as e:
            return e


class OSCMessage:
    def __init__(self, address, *msg):
        self.address = OSCAddress(address).get_bytes_addr()
        self.message = OSCArgument(*msg).get_bytes_args()

    def get_msg(self):
        self.address.extend(self.message)
        return self.address


class OSCPacket:
    def __init__(self):
        pass


# a = OSCMessage('/ciao', 1, 2, 3, 'cacca')
# print(a.get_msg())
