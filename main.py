import pyautogui as p 
from time import sleep

msg = input("Enter the message you want to spam: ")
amount = input("Enter the amount of messages to send [number]: ")
delay = input("Enter the delay time between messages (If empty - no delay): ")

try:
    amount = int(amount)
except ValueError:
    print('Please enter a valid number in amount!')
    exit()

if delay != '':
    try:
        delay = int(delay)
    except ValueError:
        print('Please enter a valid number in delay!')
        exit()

if delay == '':
    delay = 0

print("Staring...")
c = 5
while c > 0:
    sleep(1)
    print(c)
    c -= 1

i = 0
for i in range(amount):
    sleep(int(delay))
    p.typewrite(msg)
    p.press("enter")
    i += 1
