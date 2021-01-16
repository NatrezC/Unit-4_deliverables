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

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# find a random word
def word_finder(word_list):
    random_word = random.choice(word_list)
    return random_word

#game_status
def game_status(abc):
    word = word_finder(word_list) #my random word
    letters = set(abc)
    word_letters = set(word) #my random word by letters
    user_tries =  6
    used_letters = set()
    user_win = 0
    input('Press Enter to play Hangman!!')
    input('Welcome to hangman! This game will pick a random word and you have to guess that word!')
    input('You have 6 tries to get all the letters')
    input('Guess all the letters to win the game. Good Luck!')

    # print(f'your word letters is', word_letters)
    
    #keep it going!
    while len(word_letters) > 0:
        print(f'Tries count {user_tries}')
        #if letter in your word is correct then paste that letter
        right_word = [letter if letter in used_letters else '_' for letter in word]
        #joins the letters to the '_'
        print(' '.join(right_word))

        user_input = input('Choose your letter: ').lower()
        #print('random word is',word)
        #win logic
        if (''.join(right_word)) == word:
            print("You won hangman!")
            break

        if user_input in letters:
            #remove letter from abc
            letters.remove(user_input)
            #add letter to you used letter set
            used_letters.add(user_input)
            if user_input in word_letters:
                #word_letters.join(user_input)
                print('Ok that letter is in there')
                
            #if you haven't used this letter yet and it is not inside of word
            else:
                user_tries -= 1
                print('Nope!')
                #if user tries get to zero
                if user_tries == 0:
                    print('Game over! Ya lost kiddo! Your word was',word,'. Better luck next time!')
                    break

        #if function for if the letter is in the used letters
        elif user_input in used_letters:
            print('You already used that letter dude! Try a different one')
        #not a valid letter
        else:
            print('Not a letter stupid!')
            

    return user_input

def user_letter_input():
    user_input = game_status(abc)
    
    
    
    

game_status(abc)
# user_letter_input(user_input)





