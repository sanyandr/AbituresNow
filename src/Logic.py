import re
#count number of max concourse groups for student
def defineGroups(abiture):
    return len(re.findall(r'<li>\d+', abiture)) + 1

#count number of students with such priority in list
def countByPriority(abitures, priority):
    suits = 0
    stringPriority = str(priority)
    for abiture in abitures:
        if priority < defineGroups(abiture):
            if ('<li>' + stringPriority) not in abiture and ('/ ' + stringPriority + ' /') not in abiture:
                suits += 1
    return suits

#read file and write students to list, then count with priority
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