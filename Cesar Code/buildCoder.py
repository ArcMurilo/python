class CesarCode(object):
	import string

	def buildCoder(shift):
	    """
	    Returns a dict that can apply a Caesar cipher to a letter.
	    The cipher is defined by the shift value. Ignores non-letter characters
	    like punctuation, numbers, and spaces.

	    shift: 0 <= int < 26
	    returns: dict
	    """
	    assert (type(shift) == int and 0 <= shift and shift <= 26)
	    coder = {}
	    element = 1
	    for i in range(26 - shift):
	        coder[element] = string.ascii_uppercase[i + shift]
	        element += 1
	    for i in range(shift):
	        coder[element] = string.ascii_uppercase[i]
	        element += 1
	    for i in range(26 - shift):
	        coder[element] = string.ascii_lowercase[i + shift]
	        element += 1
	    for i in range(shift):
	        coder[element] = string.ascii_lowercase[i]
	        element += 1

	    return coder

	def alfabeto():
	    coder = {}
	    element = 1
	    for i in range(26):
	        coder[string.ascii_uppercase[i]] = element
	        element += 1
	    for i in range(26):
	        coder[string.ascii_lowercase[i]] = element
	        element += 1
	    return coder

	def applyCoder(text, coder):
		alf = alfabeto()
		textEncoded = ''

		for letter in text:
			if (letter in string.punctuation) or (letter == ' '):
				textEncoded += letter
				continue
			textEncoded += coder[alf[letter]]

		return textEncoded
