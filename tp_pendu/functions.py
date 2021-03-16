import os 
import pickle
from   data     import *
from   random   import choice


#TODO	A FUNCTION THAT RETURNS A DICTIONARY OF SCORES, RETRIEVES IT FROM A SERIALIZED FILE
def retrieve_scores():
	
	#Checks the existence of the file in working directory
	if os.path.exists(file_name):
		with open(file_name, "rb") as scores_file:
			unpickler = pickle.Unpickler(scores_file)
			scores = unpickler.load()	
	#If it doesn't exist we initialize scores dictionary 
	else:
		scores = {}
	return scores

#TODO	A FUNCTION TO SAVE SCORES INTO FILE (SERIALIZATION)
def save_scores(scores_dict):
	"""
	Saves a dictionary of scores into serialized file
	"""
	with open(file_name, "wb") as scores_file:
		pickler = pickle.Pickler(scores_file)
		pickler.dump(scores_dict)	

#TODO	A FUNCTION TO GET PLAYER NAME 
def get_player_name():
	"""
	Gets a player name from stdin buffer and returns it 
	"""
	player_name = str(input())
	if not player_name.isalnum():
		print("Invalid name")
		return get_player_name()
	else:
		return player_name

#TODO	A FUNCTION TO GET A LETTER FROM STDIN BUFFER
def get_letter():
	"""
	Gets letter from stdin and return it
	if the letter is valid, if not it loops until it s valid
	"""
	letter = input("enter a letter: ")
	letter = letter.lower()
	if not letter.isalpha():
		print("Invalid letter")
		return get_letter().upper() 
	else:
		return letter.upper()

#TODO	A FUNCTION TO CHOOSE A RANDOM WORD FROM A LIST OF WORDS
def choose_random_word():
	"""
	Chooses a random word form a list of words and returns it
	"""
	choosen = choice(words_list)
	word = ""
	for letter in choosen:
		if not '\n' == letter:
			word += letter
	return word

#TODO	A FUNCTION TO RETURN A MASKED WORD 
def masked_word(complete_word, found_letters):
	"""
	Returns a masked word:
	if a found letter matches a letter in complete word it prints it 
	if it doesn't match any letter in complete word it prints *
	"""
	masked_word = ""
	for letter in complete_word:
		if not letter == '\n':
			if letter in found_letters:
				masked_word += letter
			else:
				masked_word += "*"
	return masked_word
