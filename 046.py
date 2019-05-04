"""
Make a program that show in console a
countdown message with time interval of
1seg between message.
"""

from time import sleep

time = int(input('Countdown (seg): '))

for i in range(time,0,-1):
    print(i)
    sleep(1)
print('KABOOM!!!')
