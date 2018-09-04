
def hex_b64(hexadecimal):
	"""
	This functions converts hexadecimal number to base64
	"""

	return hexadecimal.decode("hex").encode("base64")


print ("Enter the hexadecimal string: ")

print  "\n" + hex_b64(input())


