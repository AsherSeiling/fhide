def regex(ref, char):
	passed = True
	for i in ref:
		if char == i:
			passed = False
	return passed