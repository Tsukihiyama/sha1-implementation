import struct
from multiprocessing import Pool

def pad_message(message):
    original_byte_len = len(message)
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', original_byte_len * 8)
    return message

def Kt(t):
    if 0<=t<=19:
        return 0x5A827999
    elif 20<=t<=39:
        return 0x6ED9EBA1
    elif 40<=t<=59:
        return 0x8F1BBCDC
    else:
        return 0xCA62C1D6

def Ch(x, y, z):
    return (x & y) ^ ((~x & 0xFFFFFFFF) & z) 

def Parity(x, y, z):
    return x ^ y ^ z

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def ft(t, x, y, z):
    if 0<=t<=19:
        return Ch(x, y, z)
    elif 20<=t<=39:
        return Parity(x, y, z)
    elif 40<=t<=59:
        return Maj(x, y, z)
    else:
        return Parity(x, y, z)

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def process_block(block):
    global H

    w = list(struct.unpack(">16I", block))
    for i in range(16, 80):
        w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))

    a, b, c, d, e = H 

    for t in range(80):
        temp = (left_rotate(a, 5) + ft(t, b, c, d) + e + w[t] + Kt(t)) & 0xFFFFFFFF
        e = d
        d = c
        c = left_rotate(b, 30)
        b = a
        a = temp

    H[0] = (H[0] + a) & 0xFFFFFFFF
    H[1] = (H[1] + b) & 0xFFFFFFFF
    H[2] = (H[2] + c) & 0xFFFFFFFF
    H[3] = (H[3] + d) & 0xFFFFFFFF
    H[4] = (H[4] + e) & 0xFFFFFFFF

def sha1(message):
    global H

    H = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]

    if isinstance(message, str):
        message = message.encode()

    message = pad_message(message)

    for i in range(0, len(message), 64):
        process_block(message[i:i+64])

    return ''.join(f'{h:08x}' for h in H)