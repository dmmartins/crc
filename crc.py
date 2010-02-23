#!/usr/bin/env python
#-*- coding: utf-8 -*-

# crc.py
# Based on http://zorc.breitbandkatze.de/crctester.c
# author: Diego Manenti Martins - dmmartins@gmail.com


'''
crc.py - Calc CRC from a string
    >>> crc16('\x01\x02\x03\x04\x05\x06\x07\x08')
    53168
    >>> crc32('\x01\x02\x03\x04\x05\x06\x07\x08')
    1070237893
'''


def reflect(s, bits=8):
    ''' Reflect bits. Eg 00101010 > 01010100. '''
    x = 1<<(bits-1)
    y = 1
    r = 0
    while x:
            if s & x:
                    r |= y
            x = x >> 1
            y = y << 1
    return r

def crc_update(bytes, order, poly, initial, final_xor, reverse):
    ''' bit by bit CRC calclation. for 1..32 bits polynom. '''
    if order < 1 or order >32:
        raise ValueError, 'Polynom order must be between 1 to 32.'

    mask = (1<<order)-1

    if poly != (poly & mask):
        raise ValueError, 'Invalid polynom.'

    if initial != (initial & mask):
        raise ValueError, 'Invalid initial value.'

    if final_xor != (final_xor & mask):
        raise ValueError, 'Invalid final XOR value.'

    if reverse:
        data = reflect
    else:
        data = lambda x, bits=None: x

    crc = data(initial, order)

    crc_high_bit = 1<<(order-1)

    for byte in bytes:
        char = data(ord(byte))
        for x in range(7, -1, -1): # 0x80 to 0x01
            bit = 1<<x

            if bool(char & bit) ^ bool(crc & crc_high_bit):
                crc = crc << 1
                crc = crc ^ poly
            else:
                crc = crc << 1

    crc = (data(crc, order) & mask) ^ final_xor

    return crc


# Predefined CRC calcs

# CRC-16
def crc16(bytes):
    '''
    CRC-16
    Order = 16
    Polynom = 0x8005
    Initial value = 0xffff
    Final XOR = 0
    '''
    return crc_update(bytes, 16, 0x8005, 0xffff, 0, True)

# CRC-32
def crc32(bytes):
    '''
    CRC-32
    Order = 32
    Polynom = 0x4c11db7
    Initial value = 0xffffffff
    Final XOR = 0xffffffff
    '''
    return crc_update(bytes, 32, 0x4c11db7, 0xffffffff, 0xffffffff, True)


if __name__ == '__main__':
    from doctest import testmod
    testmod()

