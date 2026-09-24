def lunch(money, drink, bun, people=1):
    if people == 0:
        people = 1

    total = (drink + bun) * people
    return money - total


money = int(input("Введите деньги: "))
drink = int(input("Введите цену напитка: "))
bun = int(input("Введите цену булочки: "))
people = int(input("Введите количество людей: "))

result = lunch(money, drink, bun, people)

if result > 0:
    print("Останется", result, "тенге")
elif result == 0:
    print("Хватает ровно!")
else:
    print("Не хватает", -result, "тенге")




