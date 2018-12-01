import os
import random
from Crypto.Cipher import AES

def recognize(cipher_text):

	blocks  = []
	for cpr in range(0, len(cipher_text), 16) : 
		blocks.append(cipher_text[cpr : cpr + 16]) 

	if (len(set(blocks)) == len(blocks)):
		return 'CBC'
	else:
		return 'ECB'


#https://stackoverflow.com/questions/25176447/generating-random-16-digit-number-in-python
key = os.urandom(16)
iv = os.urandom(16)
input = "S"*256

if random.randint(0,1) == 0:
	print ('ECB')
	aes = AES.new(key, AES.MODE_ECB)
	ciphertext = aes.encrypt(input)
	
else:
	print ('CBC')
	aes = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = aes.encrypt(input)

recognize(ciphertext)