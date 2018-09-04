import string

encrypted = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


for i in range(256):
	key = int(str(i), 16)
	decrypted = ""
	for j in range(len(encrypted)):
		decrypted += chr ( int(encrypted[j],16) ^ key )
	print (decrypted)
