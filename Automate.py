import random
import pyautogui as pg
import time
#apran_khunger
animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat', )
time.sleep(10)
#apran_khunger
for i in range (1000):
    a  = random.choice(animal)
    pg.write('You Are a ' + a)
    pg.press('enter')
