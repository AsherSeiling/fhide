import Modules.regularExpression as regEx
import Modules.encode as en
import Modules.decode as dec
import sys


command = sys.argv



def encrypt(shift, change, message):
	buffer = ""
	for i in message:
		if regEx.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", i) == True:
			shift += change
			if shift > 25:
				shift -= 26
		buffer += en.char_encode(i, shift)
	return buffer

def decrypt(shift, change, message):
	buffer = ""
	for i in message:
		if regEx.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", i) == True:
			shift += change
			if shift > 25:
				shift -= 26
		buffer += dec.decryption(shift, i)
	return buffer

def main():
	print(sys.argv[1])
	file1 = open(str(sys.argv[1]), "r+").read()
	file1 = file1.split("\n")
	shift = int(sys.argv[2])
	change = int(sys.argv[3])
	if sys.argv[4] == "open":
		data = []
		for i in file1:
			data.append(decrypt(shift, change, i))
		buffer = ""
		for i in data:
			buffer += f"{i}\n"
		file1 = open(sys.argv[1], "w+")
		file1.write(buffer)
	elif sys.argv[4] == "close":
		data = []
		for i in file1:
			data.append(encrypt(shift, change, i))
		buffer = ""
		for i in data:
			buffer += f"{i}\n"
		file1 = open(sys.argv[1], "w+")
		file1.write(buffer)
	else:
		print("Command error")

try:
	main()
except:
	print("fhide <file name> <shift> <change> close\nfhide <file name> <shift> <change> open")

