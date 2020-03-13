#!/usr/bin/python
#-*-coding: utf-8-*-


import numpy as np
import sys
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import datetime as dt


def checkDate(in_date):
    if dt.date.today() - in_date <= dt.timedelta(days = 6) and dt.date.today() - in_date > dt.timedelta(days=0):
        return False
    else: return True



def getWord(in_date):
    page = requests.get('https://www.dictionary.com/e/word-of-the-day/')
    soup = BeautifulSoup(page.content,'html.parser')
    wotd = (soup.find_all('div',class_="wotd-item-headword"))
    for word in range(len(wotd)):
        dates = datetime.strptime(wotd[word].find('div',class_='wotd-item-headword__date').text,'\n%A, %B %d, %Y\n').strftime('%Y-%m-%d')
        if str(in_date) == dates:
            return (wotd[word].h1.text)
    
    
def displayMan(steps):
    print("_________________")
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
    
    #in this game, the hangman is hanged in 7 steps
    while chances<7:
        
        if ''.join(play) == guess:
            print("=================\n=================\n   You Win!\n=================\n=================\n")
            sys.exit("word picked from www.dictionary.com")
            
        letter = input("Guess a letter: ").lower()

        if letter not in trials:
            if letter in guess:
               
                for x in range(len(guess)):
                  if letter == guess[x]:
                    play[x] = letter
            else:
                if letter.isalpha():
                    chances+=1
                    np.unique(trials.append(letter))
                
        print('\nWrong guesses:'+' '.join(trials)+'\n\n')
        print(' '.join(play))
        
        displayMan(chances)
        if chances == 7:
            print("    "+guess)
            print("=================\n=================\n   You Lose!\n=================\n=================\n")
            sys.exit("word picked from www.dictionary.com")

            
            
if __name__=='__main__':

    print("    ---------------------------\n\
    |   H  A  N  G  M  A  N   | \n\
    ---------------------------\n ")
    print("....Find the word, or hang the man....\n\n")
    entry = input("#Enter a date(YYYY-MM-DD) within the last seven days.\n")
    year,month,day = map(int,entry.split('-'))
    input_date = dt.date(year,month,day)
    if checkDate(input_date):
        print("=================\n=================\n   Invalid Date!\n=================\n=================\n")
        sys.exit("word picked from www.dictionary.com")
    else:
         word_in = getWord(input_date)
         playGame(word_in)
