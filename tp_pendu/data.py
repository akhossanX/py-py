

#this file contains all variables we need to use in module functions.py

#A dictionary of words from which we randomly chose one word
#TODO	LOAD SCORES FROM TXT FILE
with open("words", "r") as words:
	words_list = list(words.read().split(","))
"""
		 [
			"TYPE",
			"HELP",
			"PYTHON",
			"DEFAULT",
			"LINUX",
			"COPYRIGHT",
			"CREDIT",
			"LICENSE",
			"INFORMATION",
			"OPEN",
			"PICKLE",
			"DUMP",
			"SERIALIZED",
			"DICTIONARY",
			"LIST",
			"IMPORT",
			"TRACEBACK",
			"LOAD", 
			"KHOSSAN",
			"HIBOT",
			"MODULE"
		    ]
"""
#File in which we store players names and scores (by serialization) 
file_name = "data"


#Number of play rounds
rounds = 8
