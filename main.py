import nfc
from Crypto.Cipher import AES
import array
import sys

def connected(tag):
    keys = [tag.read(page) for page in range(0x04, 0x06)]
    combined_key = array.array('B', [item for sl in keys for item in sl]).tostring()
    obj = AES.new(combined_key, AES.MODE_CBC, 'This is iv123456')
    ciphertext = obj.encrypt('secret data which is padded with 16 bytes.......')
    print(ciphertext)
    sys.exit(0)
    return True

clf = nfc.ContactlessFrontend('usb')
tag = clf.connect(rdwr={'on-connect': connected})
