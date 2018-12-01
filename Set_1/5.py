import binascii

def Repeating_XOR(plaintext, key): 
	return bytes([plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext))])	


plaintext = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b"ICE"
ciphertext = (Repeating_XOR(plaintext, key))

print (binascii.hexlify(ciphertext).decode('ascii'))
