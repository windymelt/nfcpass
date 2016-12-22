import nfc
import os
import sys
import tagops

def connected(tag):
    tagops.generate_tag(tag)
    print("\n".join(["\t" + line for line in tag.dump()]))
    sys.exit(0)
    return True

clf = nfc.ContactlessFrontend('usb')
tag = clf.connect(rdwr={'on-connect': connected})
