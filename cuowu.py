Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('hello')
hello
>>> import random
>>> words=['chicken','dog','cat','mouse','frog']
>>> lives_remaining=14
>>> guessed_letter=''
>>> def play():
	word=pick_a_word()
	while True:
		guess=get_guess(word)
		if process_guess(guess,word):
			print('u win!well done!')
			break
		if lives_remainning==0:
			print('u r hung!')
			print('the word was:'+word)
			break
def pick_a_word():
	
SyntaxError: invalid syntax
>>> def pick_a_word():
	word_position=random.randint(0,len(words)-1)
	return words[word_position]

>>> def get_guess(word):
	print_word_with_blanks(word)
	print('lives remaining:'+str(lives_remaining))
	guess=input('guess a letter or whole word?')
	return guess

>>> def print_word_with_blanks(word):
	display_word=''
	for letter in word:
		if guessed_letters.find(letter)>-1:
			display_word=display_word+letter
		else:
			display_word=display_word+''
		print(display_word)

	
>>> def process_guess(guess,word):
	if len(guess)>-1:
		return whole_word_guess(guess,word)
	else:
		return single_word_guess(guess,word)

	
>>> def whole_word_guess(guess,word):
	global lives_remaining
	if guess==word:
		return True
	else:
		lives_remaining=lives_remaining-1
		return False

	
>>> def single_word_guess(guess,word):
	global guessed_letters
	global lives_remaining
	if word.find(guess)==-1:
		lives_remaining=lives_remaining-1
	guessed_letters=guessed_letters+guess
	if all_letters_guessed(word):
		return True
	return False

>>> def all_letters_guessed(word):
	for letter in word:
		if guessed_letters.find(letter)==-1:
			return False
		return True

	
>>> play()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    play()
NameError: name 'play' is not defined
>>> 
