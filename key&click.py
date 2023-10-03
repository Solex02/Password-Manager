import time
import pyautogui as au
import random

time.sleep(3)
print(au.position())
au.click(au.position())

pswwd = ""

for i in range(0,10):
    caracter = (chr(random.randint(65,122)))
    pswwd += caracter

print(pswwd)
au.typewrite(pswwd)
au.press('enter')

f = open("contraseña.txt", "w")
f.write(pswwd)
f.close()