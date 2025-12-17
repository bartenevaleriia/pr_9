money = int(input('Цена услуги: '))

cash = 0

while money > 0:

    while money >= 25:
        money -= 25
        cash += 1

    while money >= 10:
        money -= 10
        cash += 1

    while money >= 5:
        money -= 5
        cash += 1

    while money >= 1:
        money -= 1
        cash += 1

print(cash)

