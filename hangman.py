#!/usr/bin/python
#-*-coding: utf-8-*-


import numpy as np
import sys
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import datetime as dt


def checkDate(in_date):
    
    #check if in_date within the past 6 days
    if dt.date.today() - in_date <= dt.timedelta(days = 6) and dt.date.today() - in_date >= dt.timedelta(days=0):
        return False
    else: return True



def getWord(in_date):
    
    page = requests.get('https://www.dictionary.com/e/word-of-the-day/')
    soup = BeautifulSoup(page.content,'html.parser')
    #the variable 'seven_words' stores all word-of-the-day containers from the given webpage
    seven_words = (soup.find_all('div',class_="wotd-item-headword"))

    
    for word in range(len(seven_words)):
        #the variable 'dates' stores each date given inside each word-of-the-day container in a YYYY-MM-DD format string 
        dates = datetime.strptime(seven_words[word].find('div',class_='wotd-item-headword__date').text,'\n%A, %B %d, %Y\n').strftime('%Y-%m-%d')
        #if date is found, return word within that container
        if str(in_date) == dates:
            return (seven_words[word].h1.text)
    
    
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
    #the array 'trials' stores every new wrong guess
    trials = []
    #the variable 'play' contains the string where letters are filled on correct guessing
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
        else: print('\nYou guessed \'%s\' already' %letter)

            
            
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
        sys.exit()
    else:
         word_in = getWord(input_date)
         playGame(word_in)
