import os
path = os.getcwd()
def main():
    print(os.getcwd())
    print('1. Просмотр каталога ')
    print('2. На уровень вверх ')
    print('3. На уровень вниз ')
    print('4. Количество файлов и каталогов ')
    print('5. Размер текущего каталога (в байтах) ')
    print('6. Поиск файла ')
    print('7. Выход из программы ')
    num = acceptCommand()
    if num == 2:
        moveUp()
        return main()
    elif num == 3:
        currentDir = os.getcwd()
        moveDown(currentDir)
        return main()
    

def acceptCommand():
    try:
        a = int(input('Выберите пункт меню: '))
        if 1>a>7:
            print('Варианта с таким номером не существует. Повторите попытку. ')
            return acceptCommand()
        else:
            return a
    except ValueError:
        print('Номер пункта задан некорректно. Повторите попытку. ')
        return acceptCommand()

def moveUp():
    a = os.getcwd().rfind("\\")
    os.chdir(os.getcwd()[:a])

def moveDown(currentDir):
    currentDir = input('Введите имя каталога, в который желаете перейти: ')
    try:
        os.chdir(str(os.getcwd())+'\\'+currentDir)
    except FileNotFoundError:
        print('Указанного вами каталога не существует. Повторите попытку. ')
        return moveDown(currentDir)
main()
