print('''
===================
Rock Paper Scissors
===================

1- ✊
2- ✋
3- ✌️
''')

import random
player = 0
computer = 0

player = int(input('Pick a number: '))
print(f'You chose: {player}')

computer = random.randint(1, 3)
print(f'CPU chose: {computer}')

if player == computer:
  print('Tie!')
elif (player == 1 and computer == 3) or \
    (player == 2 and computer == 1) or \
    (player == 3 and computer == 2):
  print('The player won!')
elif (player == 1 and computer == 2) or \
    (player == 2 and computer == 3) or \
    (player == 3 and computer == 1):
  print('The computer won!')
