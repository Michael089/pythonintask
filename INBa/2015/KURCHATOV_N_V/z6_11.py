# Задача 6. Вариант 11.
#Создайте игру, в которой компьютер загадывает название
# одного из девяти действующих вокзалов Москвы, а игрок должен его угадать. 
 
# Kurchatov N. V.
# 11.04.2016

import random
x=random.randint(1,9)
if x==1:
	name="Белорусский"
elif x==2:
	name = "Казанский"
elif x==3:
	name = "Киевский"
elif x==4:
	name = "Курский"
elif x==5:
	name = "Ленинградский"
elif x==6:
	name = "Павелецкий"
elif x==7:
	name = "Рижский"
elif x==8:
	name = "Савёловский"
elif x==9:
	name = "Ярославский"	
print("Давайте поиграем в игру. Я загадываю один из девяти вокзалов Москвы, а вы должны угадать, какой именно.")	
ans=input()

while(name!=ans ):
	print("\n Не этот вокзал. Попробуешь еще угадать?")
	print ("Введите название вокзала")
	ans=input()
if name==ans:
	print("Верно! я загадал "+name+" вокзал.")
input("Нажмите Enter для выхода")