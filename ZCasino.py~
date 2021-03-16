

         #######################################################
         #######################################################
         ###### This program is a simulation of the game #######
         ######               ZCasino                    #######
         #######################################################
         #######################################################

from random import randrange
from math import ceil

# prompt user to enter his favorite number, allowed numbers between 0 and 49

print("please enter the number u want to play with")

num = int(input())
print("please enter the amount of money u want to play with")
money = int(input())

# Generating random number for the game 
winner = randrange(50)

# assertions
is_pair   = (num % 2 == 0 and winner % 2 == 0)
is_impair = (num % 2 != 0 and winner % 2 != 0)

# making tests to see whether the player won or lost
if num == winner:
    money += money * 3
    money = ceil(money)
    print "the winner number is ", winner
    print "gonrats you win ", money, "$"
elif is_pair or is_impair :
    money += money * 0.5
    money = ceil(money)
    print "the winner number is ", winner
    print "you won ", money, "$"
else:
    print "sorry, you lose ", money, "$"
    print "the winner number is ", winner


