import base64

def PAD(plaintext, block_size) : 
	text_len = len(plaintext)
	pad_len = block_size - (text_len % block_size)
	for i in range(pad_len) : 
		plaintext += chr(pad_len)
	return plaintext

plaintext = 'YELLOW SUBMARINE'
padded_text = PAD(plaintext, 20)
print (padded_text)
