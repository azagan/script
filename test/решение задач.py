#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
#которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
#то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

from math import sqrt
import datetime

def arithmetic(): #калькулятор
    while 1:
        x=int(input("Введите первое число: "))
        y=int(input("Введите второе число: "))
        z=str(input("Введите арифметический знак: "))
        if z=='+':
            print(x+y)
        elif z=='-':
            print(x-y)
        elif z=='*':
            print(x*y)
        elif z=='/':
            print(x/y)
        else:
            print("Неизвестная операция")

#arithmetic()

def is_year_leap(): #високосный ли год
    while 1:
        x=int(input("Какой сейчас год? "))
        if (x%4==0):
            print("Этот год високосный")
        else:
            print("Этот не високосный")

#is_year_leap()

def square(): #рассчет периметра, площади и диагонали по стороне квадрата
    while 1:
        x=int(input('Введите сторону квадрата: '))
        p=x*4
        s=x**2
        d=x*sqrt(2)
        a=(p, s, d)
        print("Периметр квардрата = {0}, площадь квадрата = {1}, диагональ квадрата {2}".format(a[0],a[1],a[2]))

#square()

def season():
    while 1:
        x=int(input('Введите номер месяца: '))
        if x<=2 or x==12:
            print('Сейчас зима')
        elif x<=5:
            print('Весна')
        elif x<=8:
            print('Лето')
        elif x<=11:
            print('Осень')
        else:
            print('Я не знаю что эт за месяц')

#season()

def bank(): #прибыль и процентная ставка
    while 1:
        x=int(input('Введите сумму денег, которые хотите внести: '))
        a=x
        y=int(input('А на какое количество лет?: '))
        z=int(input('Какая процентная ставка?: '))
        z=z/100 #percent
        i=0
        for i in range(0,y):
            x=x+x*z
            i+=i
        print("Общая сумма:", x)
        print("Прибыль:", x-a)
#bank()

def pascal():
    while 1:
        n=int(input("Введите Ваше число: "))
        i=0
        b=0
        g=str("")
        while n>0:
            a = n % 10
            n = n // 10
            b = a * 2
            g=str(b)+g
        print(g)
        print()
        if n == 0:
            break
        elif n == "0":
            break
pascal()

