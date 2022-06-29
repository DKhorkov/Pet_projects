import random
import os
# Чтобы работал написанный на ЧЕРЕПАХЕ модуль, нужно импортировать не только его, но и САМУ ЧЕРЕПАХУ
# Также внутри модуля не должно быть запущено функций. Иначе они сразу сработают при импортировании, а нам этого не надо
import turtle
import Turtle_Loser
import Turtle_Winner

start = input('Добро пожаловать в игру! Начнем?(да/нет):\t')
while True:
    if start.lower() == 'да':
        break
    elif start.lower() == 'нет':
        exit()
    else:
        start = input('Вы ввели что-то не то. Попробуйте снова. Начнем?(да/нет):\t')


while True:
    # Сумма атрибутов в каждом классе без учета здоровья равна 57
    elf = {'Название класса': 'Эльф', 'Сила': 10, 'Удача': 15, 'Злость': 5, 'Реакция': 7, 'Ловкость': 20,
           'Здоровье': 130}
    human = {'Название класса': 'Человек', 'Сила': 15, 'Удача': 16, 'Злость': 10, 'Реакция': 9, 'Ловкость': 7,
             'Здоровье': 110}
    dwarf = {'Название класса': 'Гном', 'Сила': 5, 'Удача': 10, 'Злость': 5, 'Реакция': 25, 'Ловкость': 7,
             'Здоровье': 150}
    ork = {'Название класса': 'Орк', 'Сила': 20, 'Удача': 5, 'Злость': 25, 'Реакция': 2, 'Ловкость': 5, 'Здоровье': 100}
    all_classes = {'Эльф': elf, 'Человек': human, 'Гном': dwarf, 'Орк': ork}


    def enumeration():
        """Данная функция создана для перечисления всех классов пользователю для дальнейшего выбора."""
        numeration = 1
        for k, v in all_classes.items():
            print(f'{numeration}) {k}\nХарактеристики класса:')
            for key, value in v.items():
                if key == 'Название класса':
                    continue
                print(f'\t{key}: {value}')
            numeration += 1


    def current_hp():
        """Функция вывод текущее здоровье пользователя и противника"""
        print(f'Ваше текущее здоровье: {user_class["Здоровье"]}')
        print(f'Текущее здоровье противника: {bot_class["Здоровье"]}')


    def bot_move():
        """Функция рандома действия бота"""
        x = random.randint(1, 2)
        return x


    enumeration()
    user_class = ''
    choice_list = ['1', '2', '3', '4']
    choice = input('\nПожалуйста, выберите класс из представленных выше.'
                   'Для выбора нажмите соответствующую клавишу (Elf - 1, Human - 2, Dwarf - 3, Ork - 4): ')
    while choice not in choice_list:
        choice = input('Ошибка. Для выбора нажмите соответствующую клавишу (Elf - 1, Human - 2, Dwarf - 3, Ork - 4): ')
    else:
        if choice == '1':
            user_class = elf
        elif choice == '2':
            user_class = human
        elif choice == '3':
            user_class = dwarf
        elif choice == '4':
            user_class = ork
    print(f'Вы выбрали класс "{user_class["Название класса"]}".')

    bot_class = random.randint(1, 3)
    if user_class == elf:
        if bot_class == 1:
            bot_class = human
        elif bot_class == 2:
            bot_class = dwarf
        elif bot_class == 3:
            bot_class = ork
    elif user_class == human:
        if bot_class == 1:
            bot_class = elf
        elif bot_class == 2:
            bot_class = dwarf
        elif bot_class == 3:
            bot_class = ork
    elif user_class == dwarf:
        if bot_class == 1:
            bot_class = elf
        elif bot_class == 2:
            bot_class = human
        elif bot_class == 3:
            bot_class = ork
    elif user_class == ork:
        if bot_class == 1:
            bot_class = elf
        elif bot_class == 2:
            bot_class = human
        elif bot_class == 3:
            bot_class = dwarf
    print(f'Противник выбрал класс "{bot_class["Название класса"]}".')

    count_moves = 0
    while user_class['Здоровье'] > 0 and bot_class['Здоровье'] > 0:
        print()
        current_hp()
        move_of_the_bot = bot_move()
        move_of_the_user = input('Ударить противника (нажмите 1) '
                                 'или попробовать заблокировать его удар (нажмите 2)?:\t')
        user_current_punch = user_class['Сила']
        bot_current_punch = bot_class['Сила']

        while not (move_of_the_user == '1' or move_of_the_user == '2'):
            try:
                move_of_the_user = input('Ошибка. Нажмите 1, чтобы ударить противника или нажмите 2, '
                                         'чтобы попробовать заблокировать его удар:\t')
            except ValueError:
                move_of_the_user = input('Ошибка. Нажмите 1, чтобы ударить противника или нажмите 2, '
                                         'чтобы попробовать заблокировать его удар:\t')
        move_of_the_user = int(move_of_the_user)

        if move_of_the_user == 2 and move_of_the_bot == 2:
            print('Никто не нанес удара.')
            continue

        if move_of_the_user == 1:
            if user_class['Злость'] > bot_class['Злость']:
                # 1 - сработал крит по боту, 2 - не сработал крит по боту
                rage_punch = random.randint(1, 2)
                if rage_punch == 1:
                    user_current_punch = int(user_current_punch * 1.5)
                    print('Пользователь впал в ярость. Критический урон.')
            #  Если у бота больше удачи, злости и ловкости, он увернется
            if user_class['Ловкость'] < bot_class['Ловкость']:
                if (user_class['Удача'] > bot_class['Удача']) or (user_class['Злость'] > bot_class['Злость']):
                    agile_random = random.randint(1, 2)
                    if agile_random == 1:
                        if move_of_the_bot == 2:
                            if (user_class['Удача'] >= bot_class['Удача']) or\
                                    (user_class['Злость'] >= bot_class['Реакция']):
                                # 1 - пробит блок бота, 2 - блок бота не пробит
                                user_block_breaking = random.randint(1, 2)
                                if user_block_breaking == 1:
                                    if user_class['Реакция'] >= bot_class['Реакция']:
                                        print('Вы пробили блок.')
                                        bot_class["Здоровье"] -= user_current_punch
                                    else:
                                        back_damage = random.randint(1, 2)
                                        if back_damage == 1:
                                            print('Вы пробили блок.')
                                            bot_class["Здоровье"] -= user_current_punch
                                        else:
                                            print('Вы пробили блок. Но и сами получили урон в ответку.')
                                            bot_class["Здоровье"] -= user_current_punch
                                            user_class["Здоровье"] -= int(user_current_punch / 2)
                                elif user_block_breaking == 2:
                                    if user_class['Реакция'] < bot_class['Реакция']:
                                        back_damage = random.randint(1, 2)
                                        if back_damage == 1:
                                            print('Вы Не пробили блок, но и ответку не получили.')
                                        else:
                                            print('Вы получили урон в ответку.')
                                            user_class["Здоровье"] -= int(user_current_punch / 2)
                                    else:
                                        print('Вы не пробили блок противника.')
                            else:
                                if user_class['Реакция'] < bot_class['Реакция']:
                                    back_damage = random.randint(1, 2)
                                    if back_damage == 1:
                                        print('Вы не пробили блок противника.')
                                    else:
                                        print('Вы получили урон в ответку.')
                                        user_class["Здоровье"] -= int(user_current_punch / 2)
                        else:
                            if user_class['Реакция'] < bot_class['Реакция']:
                                back_damage = random.randint(1, 2)
                                if back_damage == 1:
                                    print('Противник получает урон.')
                                    bot_class["Здоровье"] -= user_current_punch
                                else:
                                    print('Вы нанесли урон противнику, но и сами получили урон в ответку.')
                                    bot_class["Здоровье"] -= user_current_punch
                                    user_class["Здоровье"] -= int(user_current_punch / 2)
                            else:
                                print('Противник получает урон.')
                                bot_class["Здоровье"] -= user_current_punch
                    if agile_random == 2:
                        print('Противник увернулся.')
                        user_current_punch = 0
                        bot_class["Здоровье"] -= user_current_punch
                else:
                    print('Противник увернулся.')
                    user_current_punch = 0
                    bot_class["Здоровье"] -= user_current_punch
            elif move_of_the_bot == 2:
                if (user_class['Удача'] >= bot_class['Удача']) or\
                                    (user_class['Злость'] >= bot_class['Реакция']):
                    # 1 - пробит блок бота, 2 - блок бота не пробит
                    user_block_breaking = random.randint(1, 2)
                    if user_block_breaking == 1:
                        if user_class['Реакция'] >= bot_class['Реакция']:
                            print('Вы пробили блок.')
                            bot_class["Здоровье"] -= user_current_punch
                        else:
                            back_damage = random.randint(1, 2)
                            if back_damage == 1:
                                print('Вы пробили блок.')
                                bot_class["Здоровье"] -= user_current_punch
                            else:
                                print('Вы пробили блок. Но и сами получили урон в ответку.')
                                bot_class["Здоровье"] -= user_current_punch
                                user_class["Здоровье"] -= int(user_current_punch / 2)
                    elif user_block_breaking == 2:
                        if user_class['Реакция'] < bot_class['Реакция']:
                            back_damage = random.randint(1, 2)
                            if back_damage == 1:
                                print('Вы Не пробили блок, но и ответку не получили.')
                            else:
                                print('Вы получили урон в ответку.')
                                user_class["Здоровье"] -= int(user_current_punch / 2)
                        else:
                            print('Вы не пробили блок противника.')
                else:
                    if user_class['Реакция'] < bot_class['Реакция']:
                        back_damage = random.randint(1, 2)
                        if back_damage == 1:
                            print('Вы не пробили блок противника.')
                        else:
                            print('Вы получили урон в ответку.')
                            user_class["Здоровье"] -= int(user_current_punch / 2)
                    else:
                        print('Вы не пробили блок противника.')
            else:
                if user_class['Реакция'] < bot_class['Реакция']:
                    back_damage = random.randint(1, 2)
                    if back_damage == 1:
                        print('Противник получает урон.')
                        bot_class["Здоровье"] -= user_current_punch
                    else:
                        print('Вы нанесли урон противнику, но и сами получили урон в ответку.')
                        bot_class["Здоровье"] -= user_current_punch
                        user_class["Здоровье"] -= int(user_current_punch / 2)
                else:
                    print('Противник получает урон.')
                    bot_class["Здоровье"] -= user_current_punch

        if move_of_the_bot == 1:
            if user_class['Злость'] < bot_class['Злость']:
                # 1 - сработал крит по боту, 2 - не сработал крит по боту
                rage_punch = random.randint(1, 2)
                if rage_punch == 1:
                    bot_current_punch = int(bot_current_punch * 1.5)
                    print('Противник впал в ярость. Критический урон.')
            #  Если у пользователя больше удачи, злости и ловкости, он увернется
            if user_class['Ловкость'] > bot_class['Ловкость']:
                if (user_class['Удача'] < bot_class['Удача']) or (user_class['Злость'] < bot_class['Злость']):
                    agile_random = random.randint(1, 2)
                    if agile_random == 1:
                        if move_of_the_user == 2:
                            if (user_class['Удача'] <= bot_class['Удача']) or\
                                    (user_class['Злость'] <= bot_class['Реакция']):
                                # 1 - пробит блок user'a, 2 - блок user'a не пробит
                                bot_block_breaking = random.randint(1, 2)
                                if bot_block_breaking == 1:
                                    if user_class['Реакция'] <= bot_class['Реакция']:
                                        print('Противник пробил блок.')
                                        user_class["Здоровье"] -= bot_current_punch
                                    else:
                                        back_damage = random.randint(1, 2)
                                        if back_damage == 1:
                                            print('Противник пробил блок.')
                                            user_class["Здоровье"] -= bot_current_punch
                                        else:
                                            print('Противник пробил блок. Но и сам получил урон в ответку.')
                                            user_class["Здоровье"] -= bot_current_punch
                                            bot_class["Здоровье"] -= int(bot_current_punch / 2)
                                elif bot_block_breaking == 2:
                                    if user_class['Реакция'] > bot_class['Реакция']:
                                        back_damage = random.randint(1, 2)
                                        if back_damage == 1:
                                            print('Вы заблокировали урон от противника.')
                                        else:
                                            print('Вы заблокировали урон от противника и дали ему ответку.')
                                            bot_class["Здоровье"] -= int(bot_current_punch / 2)
                                    else:
                                        print('Противник не пробил ваш блок.')
                            else:
                                if user_class['Реакция'] > bot_class['Реакция']:
                                    back_damage = random.randint(1, 2)
                                    if back_damage == 1:
                                        print('Вы заблокировали урон от противника.')
                                    else:
                                        print('Вы заблокировали урон от противника и дали ему ответку.')
                                        bot_class["Здоровье"] -= int(bot_current_punch / 2)
                                else:
                                    print('Противник не пробил ваш блок.')
                        else:
                            if user_class['Реакция'] > bot_class['Реакция']:
                                back_damage = random.randint(1, 2)
                                if back_damage == 1:
                                    print('Противник нанес вам урон.')
                                    user_class["Здоровье"] -= bot_current_punch
                                else:
                                    print('Противник нанес вам урон, но и сам получил ответку.')
                                    user_class["Здоровье"] -= bot_current_punch
                                    bot_class["Здоровье"] -= int(bot_current_punch / 2)
                            else:
                                print('Вы получает урон.')
                                user_class["Здоровье"] -= bot_current_punch
                    if agile_random == 2:
                        print('Вы увернулись.')
                        bot_current_punch = 0
                        user_class["Здоровье"] -= bot_current_punch
                else:
                    print('Вы увернулись.')
                    bot_current_punch = 0
                    user_class["Здоровье"] -= bot_current_punch
            elif move_of_the_user == 2:
                if (user_class['Удача'] <= bot_class['Удача']) or\
                                    (user_class['Злость'] <= bot_class['Реакция']):
                    # 1 - пробит блок user'a, 2 - блок user'a не пробит
                    bot_block_breaking = random.randint(1, 2)
                    if bot_block_breaking == 1:
                        if user_class['Реакция'] < bot_class['Реакция']:
                            print('Противник пробил блок.')
                            user_class["Здоровье"] -= bot_current_punch
                        else:
                            back_damage = random.randint(1, 2)
                            if back_damage == 1:
                                print('Противник пробил блок.')
                                user_class["Здоровье"] -= bot_current_punch
                            else:
                                print('Противник пробил блок. Но и сам получил урон в ответку.')
                                user_class["Здоровье"] -= bot_current_punch
                                bot_class["Здоровье"] -= int(bot_current_punch / 2)
                    elif bot_block_breaking == 2:
                        if user_class['Реакция'] > bot_class['Реакция']:
                            back_damage = random.randint(1, 2)
                            if back_damage == 1:
                                print('Вы заблокировали урон от противника.')
                            else:
                                print('Вы заблокировали урон от противника и дали ему ответку.')
                                bot_class["Здоровье"] -= int(bot_current_punch / 2)
                        else:
                            print('Противник не пробил ваш блок.')
                else:
                    if user_class['Реакция'] > bot_class['Реакция']:
                        back_damage = random.randint(1, 2)
                        if back_damage == 1:
                            print('Вы заблокировали урон от противника.')
                        else:
                            print('Вы заблокировали урон от противника и дали ему ответку.')
                            bot_class["Здоровье"] -= int(bot_current_punch / 2)
                    else:
                        print('Противник не пробил ваш блок.')
            else:
                if user_class['Реакция'] > bot_class['Реакция']:
                    back_damage = random.randint(1, 2)
                    if back_damage == 1:
                        print('Противник нанес вам урон.')
                        user_class["Здоровье"] -= bot_current_punch
                    else:
                        print('Противник нанес вам урон, но и сам получил ответку.')
                        user_class["Здоровье"] -= bot_current_punch
                        bot_class["Здоровье"] -= int(bot_current_punch / 2)
                else:
                    print('Вы получает урон.')
                    user_class["Здоровье"] -= bot_current_punch
        count_moves += 1

    if user_class['Здоровье'] > 0 and bot_class['Здоровье'] <= 0:
        Turtle_Winner.winner()
        print(f'\nПоздравляем, вы победили за {count_moves} ходов!')
    elif user_class['Здоровье'] <= 0 and bot_class['Здоровье'] > 0:
        Turtle_Loser.loser()
        print(f'\nВы проиграли! Противник победил за {count_moves} ходов. ')
    elif user_class['Здоровье'] <= 0 and bot_class['Здоровье'] <= 0:
        print('\nНичья!')

    cont = input('\nХотите попробовать снова?(да/нет):\t').lower()
    cont_list = ['да', 'нет']
    while cont not in cont_list:
        cont = input('Ошибка. Введите "да", чтобы начать заново, или "нет", чтобы завершить программу:\t')
    if cont == 'да':
        os.system('CLS')
        continue
    elif cont == 'нет':
        break
