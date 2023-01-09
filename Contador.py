# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.CLOCK3)
    sleep(500)
    display.show(Image.ARROW_E)
    sleep(500)
    display.scroll('FRANCESCO')
