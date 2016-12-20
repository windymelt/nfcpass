import nfc
import os
import sys

def connected(tag):
    [tag.write(page, bytearray(os.urandom(4))) for page in range(0x04, 0x0f + 1)]
    print("\n".join(["\t" + line for line in tag.dump()]))
    sys.exit(0)
    return True

clf = nfc.ContactlessFrontend('usb')
tag = clf.connect(rdwr={'on-connect': connected})
