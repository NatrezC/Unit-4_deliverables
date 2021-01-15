#needs a word
#when letter of that word is correct print the letter to where the letter is suppose to be placed
#if letter is wrong then give them a strike

import random #ask questions on importing

# input('Welcome! Press enter to play hangman')
pick_number = input("Welcome to hangman! Pick a number from 0 to 7")

word_list = ['batman', 'wonderwoman', 'thor', 'ironman', 'antman', 'hulk', 'elastigirl', 'humantorch']


#print(word_list[int(pick_number)])
def word_finder(pick_number, word_list):
    num = int(pick_number)
    word = word_list[num]
    word_length = len(word)
    print(f'Your word is', word)
    print(f'The length of you word is', word_length, 'characters long')

word_finder(pick_number, word_list)

class Word():
    def __init__(self, chosen_word):
        global word_list
        self.chosen_word = random.choice(word_list)
        self.letters =  0
        self.tries = 5

    def choose_word(self):
        self.word = random.choice(word_list)
        print('your word is', self.word)









    # this method will split the word up into a list of dictionaries with 2 attributes:
    # the letter/character, and a boolean representing whether or not it has been guessed

  # ...other methods here... (refer back to JS hangman for ideas -- may not translate exactly, but
  # should be close enough)


# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop

