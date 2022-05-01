#Работу выполнили: Лысенко М. - 80%, Скороходов М. - 40%
import os
path = os.getcwd()
def main(): #Функция, выдает меню, обрабатывает запрос.
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
    elif num == 4:
        countFiles(os.getcwd())
        return main()
    elif num == 6:
        path = os.getcwd()
        extra = []
        extra = findFiles(str(input('Введите имя файла, который желаете найти: ')),path,extra)
        if not extra:
            print('Файлов с введеным именем не обнаружено.')
        else:
            print('Файлы, удовлетворяющие условиям поиска: ')
            z = -1
            for file in extra:
                z = z+1
                print(file)
    elif num == 1: #Просмотр каталога
        print('')
        print('Список файлов и директорий по текущему пути: ')
        print('')
        for item in os.scandir(os.getcwd()):
            if item.is_file():
                print(item.name,' - Файл')
            if item.is_dir():
                print(item.name,' - Директория')
        print('')
        return main()
    elif num == 5:
        path = os.getcwd()
        countBytes(path)
        return main()
    elif num == 7: #Выход из программы
        print('')
        print('Благодарим вас за то, что решили использовать наш продукт. Хорошего дня! ')
        return
def acceptCommand(): #Функция, принимает номер пункта меню, обрабатывает ошибки.
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

def moveUp(): #Подняться на каталог выше
    a = os.getcwd().rfind("\\")
    os.chdir(os.getcwd()[:a])

def moveDown(currentDir): #Спуститься на каталог ниже
    print('')
    currentDir = input('Введите имя каталога, в который желаете перейти. Если желаете вернуться назад, введите "назад": ')
    print('')
    if currentDir == 'назад':
        return main()
    else:
        try:
            os.chdir(str(os.getcwd())+'\\'+currentDir)
        except FileNotFoundError:
            print('')
            print('Указанного вами каталога не существует. Повторите попытку. ')
            print('')
            return moveDown(currentDir)

def countFiles(path): #Считает количество файлов и директорий в текущем пути
    filelist = []
    directories = []
    for a, b, c in os.walk(os.getcwd()):
        for file in c:
            filelist.append(file)
        for dir in b:
            directories.append(dir)
    print('')
    print('Количество каталогов: ' + str(len(directories)) + ' ' + 'Количество Файлов: ' + str(len(filelist)))
    print('')
    return

def findFiles(target,path,extra): #Ищет в текущем каталоге и его подкаталогах файл с указанным названием
    filecount = os.listdir(path)
    for file in filecount:
        file = str(file)
        dir = str(path)+'\\'+str(file)
        if not os.path.isdir(dir):
            if file.find(target) != 1:
                extra.append(dir)
        else:
            try:
                findFiles(target,dir,extra)
            except PermissionError:
                continue
    return extra

def countBytes(path): #Считает размер файлов (в байтах) в текущем каталоге и его подкаталогах
    a = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for files in filenames:
            a += os.path.getsize(str(dirpath)+'\\'+files)
    print('')
    print('Размер текущего каталога в байтах равен ',a)
    print('')
main()
