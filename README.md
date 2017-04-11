# crc.py

Caluculate the CRC given an input string.

    >>> from crc import CRC, CRC16, CRC32
    >>> crc16 = CRC(16, 0x8005, 0xffff, 0, True)
    >>> crc16.update('\x01\x02\x03\x04\x05\x06\x07\x08')
    53168
    >>> crc16 = CRC16()
    >>> crc16.update('\x01\x02\x03\x04\x05\x06\x07\x08')
    53168
    >>> crc16 = CRC16()
    >>> crc16.update('\x01\x02\x03\x04')
    11169
    >>> crc16.update('\x05\x06\x07\x08')
    53168
    >>> crc32 = CRC(32, 0x4c11db7, 0xffffffff, 0xffffffff, True)
    >>> crc32.update('\x01\x02\x03\x04\x05\x06\x07\x08')
    1070237893
    >>> crc32 = CRC32()
    >>> crc32.update('\x01\x02\x03\x04\x05\x06\x07\x08')
    1070237893

