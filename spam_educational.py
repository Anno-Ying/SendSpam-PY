import pyautogui as spam
import time

limit = input("Digite o número de mensagens")
msg = input("Mensagem que voce quer enviar.")

i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

i+=1