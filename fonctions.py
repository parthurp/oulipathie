_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ReorganisationAlphabetique(phrase):
	return ''.join(sorted(phrase))

def CompteLettres(phrase):
	d = dict()
	for char in _alphabet:
		d[char] = phrase.count(char)
		#print(char + ': ' + str(phrase.count(char)))
	return d

def RetireLettres(phrase1,phrase2):
	# retire de la phrase 1 les lettres contenues dans la phrase 2
	d1 = CompteLettres(phrase1)
	d2 = CompteLettres(phrase2)

	for char in _alphabet:
		d1[char]-=d2[char]
	return d1
	
def IsAnagrammeExact(phrase1,phrase2):
	return ReorganisationAlphabetique(phrase1)==ReorganisationAlphabetique(phrase2)

def IsPalindromeExact(phrase1,phrase2):
	return phrase1==phrase2[::-1]
