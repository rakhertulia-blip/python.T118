def lunch_balance(money, drink, bun):
    result = money - drink - bun
    return result


money = int(input("Сколько денег: "))
drink = int(input("Цена напитка: "))
bun = int(input("Цена булочки: "))

result = lunch_balance(money, drink, bun)

if result > 0:
    print("Останется", result, "тенге")
elif result == 0:
    print("Хватит ровно")
else:
    print("Не хватает", result, "тенге")