import random
def is_valid(number, range_):
    return 0 < number <= range_
def guess_the_number():
    print()
    print('Добро пожаловать в числовую угадайку')
    print()
    print('В каких пределах угадываем число?')
    print('от 1 до ...')
    print('Введите число:')
    range_ = input()
    random_number = random.randint(1, int(range_))
    counter = 0
    while random_number > 0:
        print(f'Введите число от 1 до {range_}')
        user_number = int(input())
        if is_valid(user_number, int(range_)):
            if user_number > random_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
                continue
            elif user_number < random_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
                continue
            else:
                print('Вы угадали, поздравляем!')
                counter += 1
                print(f'Количество попыток: {counter}')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {range_}?')
    print('Хотите сыграть ещё раз? Y/N')
    if input() == 'Y':
        guess_the_number()    
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
guess_the_number()
