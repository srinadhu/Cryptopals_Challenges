def hex_XOR(x, y):
	"""
	Two equal length buffers XOR is to be returned in hex.
	"""

	return hex( int(x,16) ^ int(y,16) )


x = input()
y = input()


print hex_XOR(x,y)[2:]
