import Modules.regularExpression as regEX
def decryption(shift, letter_char):
	char_ref = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	upper = False
	if regEX.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", letter_char) == True:
		if letter_char.isupper() == True:
			upper = True
		shift_num = char_ref.index(letter_char.lower()) - shift
		if shift_num < 0:
			shift_num += 26
		if upper == True:
			return char_ref[shift_num].upper()
		else:
			return char_ref[shift_num]
	else:
		return letter_char