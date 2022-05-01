import os
path = os.getcwd()
def main():
    print(path)
    print('1. Просмотр каталога ')
    print('2. На уровень вверх ')
    print('3. На уровень вниз ')
    print('4. Количество файлов и каталогов ')
    print('5. Размер текущего каталога (в байтах) ')
    print('6. Поиск файла ')
    print('7. Выход из программы ')
    print(acceptCommand())
    

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
    os.chdir(os.getcwd()[:os.getcwd().rfind("\\")])
moveUp()
print(os.getcwd())
