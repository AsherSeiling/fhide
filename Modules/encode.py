import Modules.regularExpression as regEx
def char_encode(char, shift):
	char_ref = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	upper = False
	# Check to eliminate all non alphabetic charicters and pass them imdediatly back
	if regEx.regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", char) == True:
		# Check if it is upper case
		if char.isupper() == True:
			upper = True
		# Get the location of the letter in the array
		letter_shifted_num = char_ref.index(char.lower()) + shift
		if letter_shifted_num > 25:
			letter_shifted_num = letter_shifted_num - 26
		con_char = char_ref[letter_shifted_num]
		# Pass back if the item is upper case or not
		if upper == True:
			return con_char.upper()
		else:
			return con_char
	else:
		return char