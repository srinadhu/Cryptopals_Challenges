import base64

ciphertext = base64.b16decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.upper())


for i in range(0, 256):
	plaintext = ""
	for j in range(0, len(ciphertext)):
		plaintext += chr(ciphertext[j] ^ i)
	print (i, plaintext)

