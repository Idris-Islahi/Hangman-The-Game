import numpy as np
import sys
from bs4 import BeautifulSoup
import requests
import datetime as dt


def checkDate():
    present = dt.datetime.now()
    last_weekend = present - dt.timedelta(days = (dt.date.weekday(present)+1))
    input_date=int(input('Input: '))
    
    #checking if input_date lies within the dates of last week(week = Monday to Sunday)
    for days in range(7):
        if input_date == ((last_weekend - dt.timedelta(days = 6-days)).day):
            return False
    else: return True


def getWord():
    url = "https://www.dictionary.com/"
    page = requests.get(url)      
    
    #parsing html content using BeautifulSoup library to find required element by class name
    elem = BeautifulSoup(page.content,'html.parser').find('a',class_="css-12ln44y ea6r3x82")

    #if the find() function falls to obtain any value, pass a default word - SPIDERMAN here- to playGame()    
    if elem == None:
        word = "SPIDERMAN"
    else: word = elem.text
    return word.lower()
    
    
def displayProgress(steps):
    if steps == 7:
        print(" |")
    
    #the hangman skeleton
    skeleton = [' O','\n/','|','\\','\n√',' \\']
    print(''.join(skeleton[:steps]))
    print("_________________\n\n")
    
    
def playGame(guess):
    chances=0
    trials = []
    
    play = ['_'] * len(guess)
    print(' '.join(play))
    
    while chances<7:
        
        if ''.join(play) == guess:
            print("=================\n=================\n   You Win!\n=================\n=================\n")
            sys.exit("word picked from www.dictionary.com")
            
        letter = input("Guess a letter: ").lower()
        print("\n")
        if letter not in trials:
            if letter in guess:
               
                for x in range(len(guess)):
                  if letter == guess[x]:
                    play[x] = letter
            else:
                if letter.isalpha():
                    chances+=1
                    np.unique(trials.append(letter))
                
        print('Wrong guesses:'+' '.join(trials)+'\n\n')
        print(' '.join(play))
        
        displayProgress(chances)
        if chances == 7:
            print("    "+guess)
            print("=================\n=================\n   You Lose!\n=================\n=================\n")
            sys.exit("word picked from www.dictionary.com")

            
            
if __name__=='__main__':
    print("    ---------------------------\n\
    |   H  A  N  G  M  A  N   | \n\
    ---------------------------\n ")
    print("....Find the word, or hang the man....\n\n")
    print("#Enter a date from last week to continue.")
    
    if checkDate():
        print("=================\n=================\n   Invalid Date!\n=================\n=================\n")
        sys.exit("word picked from www.dictionary.com")
    else:
         word_in = getWord()
         playGame(word_in)

    