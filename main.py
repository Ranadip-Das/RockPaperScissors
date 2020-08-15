import body
import random
print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))


if body.validate(player_hand):
    computer_hand = 1

    computer_hand=random.randint(0,2)

    body.print_hand(player_hand, player_name)
    body.print_hand(computer_hand, 'Computer')

    result = body.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    print('Please enter a valid number')
