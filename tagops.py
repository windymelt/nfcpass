import sys
import array

def generate_tag(tag):
    [tag.write(page, bytearray(os.urandom(4))) for page in range(0x04, 0x0f + 1)]

def read_password(tag):
    keys = [tag.read(page) for page in range(0x04, 0x06)]
    return array.array('B', [item for sl in keys for item in sl]).tostring()
