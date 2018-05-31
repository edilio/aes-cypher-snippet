# aes-cypher-snippet
Snippet for encrypting/decrypting messages in python using Cryto.Cypher AES

## Requirements
pycrypto==2.6.1

## How to test it


* cp sample.env .env
* edit .env changing your SECRET_KEY
* source .env && ./cypher.py

## The snippets

```python
def encrypt(msg):
    """
    msg should be multiple of 16
    """
    msg16 = msg + ' '*(16 - len(msg) % 16)
    obj = AES.new(SECRET_KEY[:16], AES.MODE_CBC, SECRET_KEY[-16:])
    encrypted = obj.encrypt(msg16)
    return base64.b64encode(encrypted)
```

```python
def decrypt(msg):
    dec_msg = base64.b64decode(msg)
    obj = AES.new(SECRET_KEY[:16], AES.MODE_CBC, SECRET_KEY[-16:])
    return obj.decrypt(dec_msg).strip()
```
