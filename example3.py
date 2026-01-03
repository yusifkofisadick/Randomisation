# The Lucky number game
import random
user = int(input("input a Lucky number 1-5"))

random_num = random.randint(1,5)

if random_num == user:
    print(random_num)
    print('You win')


elif user >5:
    print("invalid number. Try again")


else:
    print(random_num)
    print('You Lose')


