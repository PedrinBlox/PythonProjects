# github.com/PedrinBlox
import random
import os

class Game:
    def end(self):
        os.system('pause')
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        try:
            number = random.randint(1, 100)
            
            while True:
                guess = int(input('Pick a number between 1-100: '))

                if guess < number:
                    print('Your choice is lower than the number!')
                
                elif guess > number:
                    print('Your choice is higher than the number!')

                elif guess == number:
                    print(f'You won! The number was {number}.')
                    break
        except Exception:
            print('An error occurred')
        finally:
            self.end()

game = Game()

while True:
    game.start()
