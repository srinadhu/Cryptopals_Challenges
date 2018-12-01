import base64
from Crypto.Cipher import AES

key = 'YELLOW SUBMARINE'
cipher_text = base64.b64decode(open('7.txt', 'r').read())
cipher = AES.new(key, AES.MODE_ECB)
plain_text = cipher.decrypt(cipher_text)
print(plain_text)
