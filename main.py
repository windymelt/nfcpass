import nfc
from simple_aes_cipher import AESCipher, generate_secret_key
import array
import sys
import base64

def connected(tag):
    keys = [tag.read(page) for page in range(0x04, 0x06)]
    combined_key = array.array('B', [item for sl in keys for item in sl]).tostring()
    obj = AESCipher(combined_key)
    #ciphertext = obj.encrypt('secret data')
    #b64ciphertext = base64.b64encode(ciphertext)
    #print(b64ciphertext)
    with open('secret.base64', 'r') as f:
        print(obj.decrypt(base64.b64decode(f.readline())))
    sys.exit(0)
    return True

clf = nfc.ContactlessFrontend('usb')
tag = clf.connect(rdwr={'on-connect': connected})
