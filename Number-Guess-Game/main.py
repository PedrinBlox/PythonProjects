# github.com/PedrinBlox
import random
import os

class Game:
    def end(self):
        os.system('pause')
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        number = random.randint(1, 100)

        guess = int(input('Pick a number between 1-100: '))

        if type(guess) != int:
            print('Invalid choice')
            self.end()

        if guess < number:
            print('Your choice is lower than the number!')
        
        if guess > number:
            print('Your choice is higher than the number!')

        if guess == number:
            print(f'You won! The number was {number}.')
            self.end()

game = Game()

while True:
    game.start()