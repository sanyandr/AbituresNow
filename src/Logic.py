import re
def defineGroups(abiture):
    return len(re.findall(r'<li>\d+', abiture)) + 1

def countByPriority(abitures, priority):
    suits = 0
    stringPriority = str(priority)
    print(abitures[0])
    if ('<li>' + stringPriority not in abitures[0].strip()): print("HUUUUUUI")
    for abiture in abitures:
        if priority < defineGroups(abiture):
            if ('<li>' + stringPriority) and ('/ ' + stringPriority + ' /') not in abiture:
                suits += 1
    return suits

def calculateAbitures(priority):
    abitures = []
    stringAbiture = ''

    # получим объект файла
    file1 = open("filename.txt", "r", encoding="utf-8")
    # считываем все строки
    lines = file1.readlines()
    lines += '\nend'

    # итерация по строкам
    for line in lines:
        if line != '\n':
                stringAbiture += line.strip() 
        else:
            if (stringAbiture != ''):
                abitures.append(stringAbiture)
            stringAbiture = ''

    # закрываем файл
    file1.close
    return countByPriority(abitures, priority)


#ВЫЗОВ базы
print(calculateAbitures(2))
