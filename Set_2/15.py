def unpad(s):
    if s[-1] == 0 or s[-s[-1]:] != bytes([s[-1]] * s[-1]):
        return 'invalid'
    return 'valid'

print(unpad(b'ICE ICE BABY\x04\x04\x04\x04'))
print(unpad(b'ICE ICE BABY\x05\x05\x05\x05'))
print(unpad(b'ICE ICE BABY\x01\x02\x03\x04'))
