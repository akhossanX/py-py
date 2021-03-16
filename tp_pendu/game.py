
from functions import *
from data import *

print(" Welcome to Pendu Game ...")
print("Please enter your name")
player_name = get_player_name()
scores = retrieve_scores()

continue_game = 'y'
while continue_game == 'y':
	if not  player_name in scores.keys():
		scores[player_name] = 0

	found_letters = []
	complete_word = choose_random_word()

	while rounds > 0 and masked_word(complete_word, found_letters) != complete_word:
		print("Choose a letter ( u still have {} tries)".format(rounds))
		choosen_letter = get_letter()
		while choosen_letter in found_letters:
			print("You ve already found that letter, try another one")
			choosen_letter = get_letter()

		if choosen_letter in complete_word:
			found_letters.append(choosen_letter)
		rounds-= 1
		print("you still have {} tries".format(rounds))
		print(masked_word(complete_word, found_letters))

	if masked_word(complete_word, found_letters) == complete_word :
		scores[player_name] += rounds
		print("Congratulation you won the game")
		print("your score is {}".format(scores[player_name]))
		print("Press Y if you want to replay, N to quit the game")
		continue_game = input()
	else:
		print("Sorry , you lost the game, the word is {}".format(complete_word))
		print("Press Y if you want to replay, N to quit the game")
		continue_game = input()
		
	save_scores(scores)
	#Reset the rounds to intial value 8
	rounds = 8

#The player ended the game
print("Thank you for playing Pendu Game, Byeeeee!!!!! ;-)")

