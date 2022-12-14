
from math import * 
from random import * 
#1
n = int(input("Sisestage number: "))
if(n > 0):
    print("Arv on positiivne")
else:
    print("Arv on negatiivne")


from math import * 
from random import * 
#2
num1 = int(input("первый номер:"))
num2 = int(input("второй, номер:"))
num3 = int(input("третий номер:"))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1+num2+num3==180:
        if num1==num2==num3==180:
           print("цифры обозначают углы равностороннего треугольника.")
        elif num1==num2 or num1==num3 or num2==num3:
            print("цифры обозначают углы равнобедренного треугольника.")
        else:
            print("цифры обозначают углы равностороннего треугольника.")
    else:
        print("Не углы!")
else:
    print("Ошибка!")


from math import * 
from random import * 
#3
kusimus=input("Хочешь узнать день недели?")
if kusimus.lower()=="jah":
    number=input("Введите число от 1 до 7: ")
    if number.isdigit() and 1<=int(number) <= 7:
        days=["понедельние, вторник, среда, четверг, пятница, суббота, воскресенье"]
        print(f"день недели: {days[int(number)-1]}")
    else:
        print("ошибка!")
else:
    print("хорошо!")