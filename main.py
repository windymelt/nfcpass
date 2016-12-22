import nfc
from simple_aes_cipher import AESCipher, generate_secret_key
import sys
import base64
import tagops

def connected(tag):
    print >> sys.stderr, 'tag touched'
    obj = AESCipher(tagops.read_password(tag))
    #ciphertext = obj.encrypt('secret data')
    #b64ciphertext = base64.b64encode(ciphertext)
    #print(b64ciphertext)
    with open('secret.base64', 'r') as f:
        print(obj.decrypt(base64.b64decode(f.readline())))
#    sys.exit(0)
    return True

with nfc.ContactlessFrontend('usb') as clf:
    while clf.connect(rdwr={'on-connect': connected}):
        print >> sys.stderr, 'tag released'
