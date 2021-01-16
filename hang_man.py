# create an array with random words
# create a function for the random word to be chosen
# create a function to be able to track how many letters are inside of the array
# for however many letters that are in the word add '_'
# have the function to allow only 6 tries to guess
# user is be able to guess the letters
# if user letter = true place letter in appropriate spot / let the user know how many tries that they have
# if user letter = false remove a try from the allowed try / also let user know how many tries that he has left
# allow the user to know if they have already chosen the letter... if user have then let user know and do not count their try against them
# if user uses all tries... acknowledge that they have lost
# if user guesses the word... acknowledge that user have won

import random #ask questions on importing



word_list = ['batman', 'wonderwoman', 'thor', 'ironman', 'antman', 'hulk', 'elastigirl', 'humantorch', 'dash', 'blackpanther','megaman','wolverine','superman','elektra','daredevil','atom','aquaman','wasp','flash','staticshock','mrfantastic','robin']

    
def word_finder(word_list):
    random_word = random.choice(word_list)
    return random_word

def user_status():
    word = word_finder(word_list)
    word_letter = len(word)
    user_tries =  6
    return word, word_letter, user_tries

def user_plays():
    user_tries = 6
    
    


user_status()


    



