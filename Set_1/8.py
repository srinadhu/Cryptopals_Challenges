import base64
from Crypto.Cipher import AES

def ECB(text): 
	chunks = []
	for elem in range(0, len(text), AES.block_size) : 
		if AES.block_size + elem < len(text) : 
			chunks.append(text[elem:elem + AES.block_size]) 

	if len(chunks) != len(set(chunks)) : 
		print ('Yes! ECB: ',text)

f = open("8.txt", 'r')

for line in f: 
	ECB(base64.b16decode(line.strip().upper()))
