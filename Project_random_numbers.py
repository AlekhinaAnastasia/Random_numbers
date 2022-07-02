from random import *
print('Добро пожаловать в числовую угадайку')

def is_valid(k):
    if k.isdigit():
        k = int(k)
        if 1 <= k <= 100:
            return True
        else:
            return False
    else:
        return False

def is_valid_right(p):
    if p.isdigit() != True:
        return False
    if int(p) < 2:
        return False
    return True

def number_input():
    while True:
        number = input('Введите число:', )
        if is_valid(number) == True:
            return int(number)
        else:
            print('А может быть все-таки введем целое число от 1 до', game_range, '?')

def game():
    global game_range
    game_range = input("Введите правую границу диапазона для игры(от 1 до ___):")
    while is_valid_right(game_range) != True:
        print("Необходимо ввести именно число(от двух и больше, чтобы игра работала")
        game_range = input("Введите правую границу диапазона для игры(от 1 до ___):")
    random_number = randint(1, int(game_range))
    counter = 0
    while True:
        number = int(number_input())
        counter += 1
        if number < random_number:
           print('Ваше число меньше загаданного, попробуйте еще разок')
           continue
        elif number > random_number:
           print('Ваше число больше загаданного, попробуйте еще разок')
           continue
        else:
           print('Вы угадали число поздравляем!', 'Было совершено', counter, 'попыток')
           while True:
               answer = input('Хотите сыграть еще раз?(да/нет):', )
               if answer == 'да':
                     print("Отлично! Продолжим...")
                     game()
               elif answer == 'нет':
                   print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                   break
               else:
                   print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
                   continue
game()