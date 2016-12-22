import nfc
from simple_aes_cipher import AESCipher, generate_secret_key
import sys
import base64
import tagops

def connected(tag):
    print >> sys.stderr, 'tag touched. input password and send return'
    obj = AESCipher(tagops.read_password(tag))
    ciphertext = obj.encrypt(raw_input())
    b64ciphertext = base64.b64encode(ciphertext)
    print(b64ciphertext)
    sys.exit(0)
    return True

with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': connected})
