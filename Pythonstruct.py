import base64, struct

with open('test.bmp', 'rb') as f:
    s = f.read(30)

print(s)
def bmp_info():
    t = struct.unpack('<ccIIIIIIHH', s)
    if (t[0] != b'B' or t[1] != b'M'):
        print('test')
        return None
    else:
        return {
            'width' : t[6],
            'height': t[7],
            'color' : t[9]
        }

bi = bmp_info()
print(bi['width'], bi['height'], bi['color'])
