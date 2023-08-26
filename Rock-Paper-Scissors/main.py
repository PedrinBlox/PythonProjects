# github.com/PedrinBlox
import random
import os

machine_wins = 0
human_wins = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'Machine wins: {machine_wins}')
    print(f'Your wins: {human_wins}')
    print()

    choice = str(input('rock/paper/scissors, type here: '))

    machine_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f'Machine chose: {machine_choice}')

    if not choice in ['rock', 'paper', 'scissors']:
        print('Your choice is invalid!')

    # rock
    if choice == 'rock' and machine_choice == 'paper':
        print('Machine won!')
        machine_wins += 1
    
    if choice == 'rock' and machine_choice == 'rock':
        print('Tied!')

    if choice == 'rock' and machine_choice == 'scissors':
        print('You won!')
        human_wins += 1

    # paper
    if choice == 'paper' and machine_choice == 'scissors':
        print('Machine won!')
        machine_wins += 1
    
    if choice == 'paper' and machine_choice == 'paper':
        print('Tied!')

    if choice == 'paper' and machine_choice == 'rock':
        print('You won!')
        human_wins += 1

    # scissors
    if choice == 'scissors' and machine_choice == 'rock':
        print('Machine won!')
        machine_wins += 1
    
    if choice == 'scissors' and machine_choice == 'scissors':
        print('Tied!')

    if choice == 'scissors' and machine_choice == 'paper':
        print('You won!')
        human_wins += 1

    os.system('pause')