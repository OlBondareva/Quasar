#This small numeric game based on rules described in "Mass Effect". 
#Pls. see additional description here: https://masseffect.fandom.com/ru/wiki/Квазар
 
def Introduction(): # Начало игры, описание функции 
    print('''Привет, мой кожаный друг!
Cыграй со мной в Квазар.
''')

def End(): #Вариант окончния игры №1 
    print('''Скайнет поработил человечество, и тебя, между прочим, тоже!  
''')   

def End1(): #Вариант окончния игры №2 
    print('''Это чит, человек! Скайнет победил!
''')

print('''Компьютер выбрасывает случайную цифру, 
игрок добавляет к ней на выбор число в диапазоне 4–7 либо в диапазоне 1–8. 
Правила напоминают блек-джек: задача игрока — как можно быстрее довести сумму очков до двадцати, 
но не превысить это число...''') #Это описание правил 
print()
print()
Introduction() #вызов "Введения", 

import time
print("Сперва я загадаю число")
print("*Cкайнет думает...*")
time.sleep(2)

import random
ComputerNumber=random.randint(1, 19)
print(ComputerNumber)

Taken=int(input('Теперь ты - введи целое число в диапозоне 1-8 : ')) #первая развилка
if Taken > 20:
    time.sleep(2)
    End1() #Второй вариант окончания игры
        
else:
   Result=Taken+ComputerNumber
   print ("Сумма очков:") 
   print(Result)

if Result == 20:
    print('Ты выиграл! =(')
elif 0 <= Result <= 19:
    print('''Продолжаем играть, мой кожаный друг, сейчас я задумаю число:''')
    ComputerNumber1=random.randint(1, 6)
    print(ComputerNumber1)

    Result1=ComputerNumber1+Result
    print ("Текущая сумма очков:")
    print(Result1)
    
elif Result > 20
   End() #вызов окончания игры №1 

else:
    End() #вызов окончания игры №1 


