#!/usr/bin/env python

import os

import base64
from Crypto.Cipher import AES


SECRET_KEY = os.environ.get('SECRET_KEY')


def encrypt(msg):
    """
    msg should be multiple of 16
    """
    msg16 = msg + ' '*(16 - len(msg) % 16)
    obj = AES.new(SECRET_KEY[:16], AES.MODE_CBC, SECRET_KEY[-16:])
    encrypted = obj.encrypt(msg16)
    return base64.b64encode(encrypted)


def decrypt(msg):
    dec_msg = base64.b64decode(msg)
    obj = AES.new(SECRET_KEY[:16], AES.MODE_CBC, SECRET_KEY[-16:])
    return obj.decrypt(dec_msg).strip()


def main():
    msg = 'edilio gallardo snippet is being tested here'
    print('Original message is: {}'.format(msg))
    cypher_text = encrypt(msg)
    print('cypher_text: {}'.format(cypher_text))
    orig_msg = decrypt(cypher_text)
    print('Original message was: {}'.format(orig_msg))
    assert msg == orig_msg


if __name__ == '__main__':
    main()
