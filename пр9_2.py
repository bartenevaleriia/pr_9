print('Введите имена игроков. Для окончания списка - пустая строка')
name = input()
num = 0
alexandra = -1
levon = -1
while name != '':
    if name == 'Александра' or name == 'александра':
        alexandra = num
    if name == 'Левон' or name == 'левон':
        levon = num
    num +=1
    name = input()
if alexandra >= 0 and levon > alexandra:
    between = levon - alexandra - 1
else:
    between = 0
print('Между Александрой и Левоном:', between)