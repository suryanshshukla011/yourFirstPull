#This code can be used to print multiple things any no.of times.
#By setting the loop value you print random text from the given list.
#Can be used in multiple ways.
#You just have to run the code, then take your cursor to the specified place where you want your output.
#First left click the mouse and then press "ENTER" Key.

import random 
#@python.coder_

import pyautogui as pg

import time

text=("java","c++","html","css","mysql","Kotlin","JavaScript")

time.sleep(8)
 
for i in range(100):
	a=random.choice(text)
	pg.write("Python & "+a)
	pg.press('enter')
	
    #----by ARPIT RAJ
	#GitHub- @arpit-raj04