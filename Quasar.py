
print('''Компьютер выбрасывает случайную цифру, 
игрок добавляет к ней на выбор число в диапазоне 4–7 либо в диапазоне 1–8. 
Правила напоминают блек-джек: задача игрока — как можно быстрее довести сумму очков до двадцати, 
но не превысить это число...''')
print()
print()
print('''Привет, мой кожаный друг!
Cыграй со Skynet в Квазар.
''')

import time
print("Сперва я загадаю число")
print("*Cкайнет думает...*")
time.sleep(2)

import random
ComputerNumber=random.randint(1, 19)
print(ComputerNumber)

Taken=int(input('Теперь ты - введи целое число : '))
Result=Taken+ComputerNumber
print ("Сумма очков:")
print(Result)

if Result == 20:
    print('Ты выиграл! =(')
elif 0 <= Result <= 19:
    print('''Продолжаем играть, мой кожаный друг, сейчас я задумаю число:''')
    ComputerNumber=random.randint(1, 19)
    print(ComputerNumber)
else:
    print('Увы, это больше 20, Скайнет поработил человечество')


