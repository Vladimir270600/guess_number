from random import randint

number = randint(1,100)
print('Угадай число от 1 до 100.')

while True:
    guess = int(input('Введите число: '))
    if guess < number:
        print('Ваше число меньше, загаданого.')
    elif guess > number:
            print('Ваше число больше, загаданого.')
    elif guess == number:
        break
print('Поздравляю, вы угадали загаданое число.')