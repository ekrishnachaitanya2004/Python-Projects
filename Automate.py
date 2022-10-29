#ekc2004
import random
#random library can pick random strings that are defined in program
import pyautogui as pg
#pyautogui is a python libray that can write,press the letters as user typed.
import time
animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat', )
time.sleep(10)
#here sleep time is set to 10sec,because some defenders can find it as bot
for i in range (1000):
    a  = random.choice(animal)
    pg.write('You Are a ' + a)
    pg.press('enter')
