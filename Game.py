
print('Game\n')

import sys

def like():
    like = input('Любите ли Вы играть?(Да/Нет)\t')
    if like.lower() == 'да':
        return True
    else:
        return False

gamer = {'name': input('Как Вас зовут?\t'),
         'age': int(input('Сколько Вам лет?\t')),
         'sex': input('Укажите пол(М/Ж):\t'),
         'pet_name': input('Кличка домашнего животного:\t'),
         }
like()

if gamer['age'] < 18:
    print('Вам нельзя играть')
elif gamer['age'] > 90:
    print('Игра может Вас утомить')
    answer = input('Вы уверены, что хотите играть?(Да/Нет)\t')
    if answer.lower() == 'да':
        print('Хорошо, тогда начнем игру.')
    else:
        print('До свидания,', gamer['name'])
        sys.exit()
else:
    print('Добро пожаловать в игру,', gamer['name'])

print('Я могу назвать буквы алфавита, которых нет в твоем имени')

abc = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',)
i = 0
for char in abc:
    i += 1
    if char in gamer['name'].lower():
        continue
    print(char)

print('Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. Скажите мне, где какое.')

line = [1, 5, 10, 7, 11, 13, 4, 8, 15, 3, 16, 14, 2, 6, 12, 9]
closed_line = '|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|'
print(closed_line)
opened_lst = closed_line[1:-1].split('|')

n = 1
moves = 0
while n in line:
    print('\nГде число', n, '?')
    answer = int(input('Введите номер ячейки:\t'))
    moves += 1
    if n == line[answer - 1]:
        print('Да, действительно верно.')
        opened_lst[answer - 1] = n
        print('|', end = '')
        for i in range(16):
            print(opened_lst[i], end = '|')
        n += 1
    else:
        print('Нет, не верно, попробуйте еще раз.')
        continue
print('\nКоличество ходов:\t', moves)