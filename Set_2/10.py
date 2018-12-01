import base64
from Crypto.Cipher import AES

def xor(present, previous):
    return bytes(a ^ b for a, b in zip(present, previous))


def decrypt(cipher_text, IV, key) : 

	Aes= AES.new(key, AES.MODE_ECB)
	
	plaintext = ""

	blocks  = []
	for cpr in range(0, len(cipher_text), 16) : 
		blocks.append(cipher_text[cpr : cpr + 16]) 

	prev_block = IV

	for block in blocks :
		decrypted_block =  xor(Aes.decrypt(block), prev_block)
		plaintext += str(decrypted_block)
		prev_block = block

	return plaintext


with open("10.txt") as file : 
	cipher_text = base64.b64decode(file.read())
iv = bytes([0]*16)
key = b'YELLOW SUBMARINE'
plaintext = decrypt(cipher_text, iv, key)
print(plaintext)

