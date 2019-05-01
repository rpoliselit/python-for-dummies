"""
Make a jokenpo game (rock-paper-scissors).
"""
from random import choice
from time import sleep

dic1 = {'rock' : 1 , 'paper' : 2 , 'scissors' : 3}
dic2 = {1 : 'rock' , 2 : 'paper' , 3 : 'scissors'}

list = [1,2,3]
cpu = choice(list)

print("""
Choose your destine!
-----------------------
Rock, Paper or Scissors
-----------------------
""")

player = dic1[input('Pick one (type): ').strip()]

print('CPU is choosing...')
sleep(2)
print('Done!')
sleep(1)
print('JO-')
sleep(1)
print(' -KEN-')
sleep(1)
print('    -PO!')
sleep(1)


if player == cpu:
    print('----!DRAW!----')
elif (player == dic1['rock'] and cpu == dic1['scissors'])\
     or (player == dic1['paper'] and cpu == dic1['rock'])\
     or (player == dic1['scissors'] and cpu == dic1['paper']):
    print('YOU WIN!!!!')
else:
    print('You lose...')

print('Player: {}!\nCPU: {}!'.format(dic2[int(player)],dic2[int(cpu)]))
