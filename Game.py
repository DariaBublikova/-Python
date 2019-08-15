
print('Game\n')

import sys

def like():
    like = input('Любите ли Вы играть?(Да/Нет)\t')
    if like == 'Да':
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
    if answer == 'Да':
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
