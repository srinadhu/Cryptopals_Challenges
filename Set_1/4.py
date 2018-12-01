import string

max_count = 0
plain_text = ""

f = open("4.txt", 'r')

for line in f: 
	line = line.rstrip()
	line = bytearray.fromhex(line)
	for i in range(256) :
		count = 0 
		plain_text_key = ""
		for char in line : 
			pchar = chr(char ^ i)
			plain_text_key += pchar
			if (pchar in string.ascii_letters or pchar == " "):  #space should be kept otherwise wrong answer
				 count += 1
		if count >= max_count : 
			max_count = count
			plain_text = plain_text_key

print (plain_text)