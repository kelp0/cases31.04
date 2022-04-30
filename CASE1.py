#Работу выполнили Лысенко М. - 80%, Скороходов М. - 35%
import turtle
import math
t = turtle.Turtle()
def kvadrat(n,s): #Тренировочный квадрат
    if n == 0:
        forward(s)
    else:
        t.speed(500)
        t.down()
        t.forward(s)
        t.right(90)
        t.forward(s)
        t.right(90)
        t.forward(s)
        t.right(90)
        t.forward(s)
        t.right(90)
        t.up()
        t.right(10)
        t.forward(s/10)
        t.down()
        try:
            kvadrat(n-1,s/10*9/math.cos(0.174533))
        except NameError:
            return
def branch(n, size): #Ветка
    if n == 0:
        t.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)

def koch(order, size): #Кривая Коха
    if order == 0:          
        t.forward(size)
    else:
        koch(order-1, size/3)   
        t.left(60)
        koch(order-1, size/3)
        t.right(120)
        koch(order-1, size/3)
        t.left(60)
        koch(order-1, size/3)

def snezhinka(n, size): #Снежинка Коха
    koch(n, size)
    t.right(120)
    koch(n, size)
    t.right(120)
    koch(n, size)
    t.right(120)


def minkovsky(n, size): #Кривая Минковского
    if n == 0:
        t.forward(size)
    else:
        minkovsky(n-1,size/4)
        t.left(90)
        minkovsky(n-1,size/4)
        t.right(90)
        minkovsky(n-1,size/4)
        t.right(90)
        minkovsky(n-1,2*size/4)
        t.left(90)
        minkovsky(n-1,size/4)
        t.left(90)
        minkovsky(n-1,size/4)
        t.right(90)
        minkovsky(n-1,size/4)


def icy(n,size): #Ледяной фрактал 1
    if n == 0:
        t.forward(size)
    else:
        icy(n-1,size/2)
        t.left(90)
        icy(n-1,size/4)
        t.right(180)
        icy(n-1,size/4)
        t.left(90)
        icy(n-1,size/2)

def icy1(n,size): #Ледяной фрактал 2
    if n == 0:
        t.forward(size)
    else:
        icy1(n-1,size/2)
        t.left(120)
        icy1(n-1,size/4)
        t.left(180)
        icy1(n-1,size/4)
        t.left(120)
        icy1(n-1,size/4)
        t.left(180)
        icy1(n-1,size/4)
        t.left(120)
        icy1(n-1,size/2)


def levi(n,size): #Кривая Леви
    if n == 0:
        t.forward(size)
    else:
        t.left(45)
        levi(n-1,size/2)
        t.right(90)
        levi(n-1,size/2)
        t.left(45)


def dragon(n, size): #Дракон Хартера-Хейтуэя
    if n == 0:
        t.forward(size)
    else:
        t.left(45)
        dragon(n-1,size/2**0.5)
        t.right(90)
        t.up()
        t.forward(size/2**0.5)
        t.down()
        t.right(180)
        dragon(n-1,size/2**0.5)
        t.right(180)
        t.up()
        t.forward(size/2**0.5)
        t.down()
        t.left(45)

def tree(size,a): #Двоичное дерево
    if size<30:
        return
    else:
        t.forward(size)
        t.left(a)
        tree(size*0.75,a)
        t.right(2*a)
        tree(size*0.75,a)
        t.left(a)
        t.backward(size)


def own(n,size): #Свой фрактал
    if n == 0:
        t.forward(size)
    else:
        own(n-1,size/2)
        t.left(135)
        own(n-1,size/4)
        t.right(90)
        own(n-1,size/4)
        t.right(90)
        own(n-1,size/4)
        t.right(90)
        own(n-1,size/4)
        t.left(135)
        own(n-1,size/2)


def nnn(): #Функция, запрашивающая глубину фрактала
    try:
        n = int(input('Введите глубину фрактала: '))
        if n<0:
            print('Глубина фрактала должна быть неотрицательной. Повторите попытку.')
            return nnn()
        else:
            return n
    except ValueError:
        print('Глубина фрактала задается целым числом. Повторите попытку.')
        return nnn()
    
def sizee(): #Функция, запрашивающая размер фрактала
    try:
        size = float(input('Введите размер фрактала: '))
        if size<=0:
            print('Размер фрактала должна быть больше нуля. Повторите попытку.')
            return sizee()
        else:
            return size
    except ValueError:
        print('Размер фрактала задается действительным числом. Повторите попытку.')
        return sizee()
    
def anglee(): #Функция, запрашивающая угол дерева
    try:
        angle = float(input('Введите угол наклона веток: '))
        if angle<=0:
            print('Угол должен быть больше нуля. Повторите попытку.')
            return anglee()
        else:
            return angle
    except ValueError:
        print('Угол задается действительным числом. Повторите попытку.')
        return anglee()

def number(): #Функция, запрашивающая номер фрактала
    try:
        a = int(input('Введите номер, под которым находится желаемый фрактал: '))
        if a>11 or a<1:
           print('Фрактала с таким номером не существует. Повторите попытку.')
           return number()
        else:
            return a
    except ValueError:
        print('Вероятно, вы допустили ошибку при вводе номера. Номер - это число. Повторите попытку. ')
        return number()
        
def main():
    t.speed(500)
    print('Фракталы, доступные для построения:')
    print('1. Квадрат')
    print('2. Двоичное дерево')
    print('3. Ветка')
    print('4. Кривая Коха')
    print('5. Снежинка Коха')
    print('6. Кривая Минковского')
    print('7. Ледяной фрактал #1')
    print('8. Ледяной фрактал #2')
    print('9. Кривая Леви')
    print('10. Дракон Хартера-Хейтуэя')
    print('11. "Свой" фрактал')
    a = number()
    if a == 1:
        n = nnn()
        size = sizee()
        kvadrat(n,size)
    elif a == 2:
        size = sizee()
        a = anglee()
        t.left(90)
        tree(size,a)
    elif a == 3:
        n = nnn()
        size = sizee()
        t.left(90)
        branch(n,size)
    elif a == 4:
        n = nnn()
        size = sizee()
        koch(n,size)
    elif a == 5:
        n = nnn()
        size = sizee()
        snezhinka(n,size)
    elif a == 6:
        n = nnn()
        size = sizee()
        minkovsky(n,size)
    elif a == 7:
        n = nnn()
        size = sizee()
        icy(n, size)
    elif a == 8:
        n = nnn()
        size = sizee()
        icy1(n,size)
    elif a == 9:
        n = nnn()
        size = sizee()
        levi(n,size)
    elif a == 10:
        n = nnn()
        size = sizee()
        dragon(n,size)
    elif a == 11:
        n = nnn()
        size = sizee()
        own(n, size)
main()
    
