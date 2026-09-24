# 1 два имени с одинаковым названием

city="Алматы"

def show_trip():
  city="Шымкент"
  print("Поездка EKEB:",city)
show_trip()
print("Исходный город:",city)

# 2 стоимость обеда в ЕКЕВ
total=10000
def lunch_total(price,guantity):
    total=price*guantity
    return total
result=lunch_total(1200,3)
print(result)
print(total)
result=lunch_total(1200,0)
print(result)
print(total)
result=lunch_total(0,2)
print(result)
print(total)

# 3 общий счетчик найденных ошибок
bugs_found=0
def register_bugs(amount):
      global bugs_found
      bugs_found += amount
      return bugs_found
print(register_bugs(2))
print(bugs_found)
print(register_bugs(3))
print(bugs_found)
print(register_bugs(0))
print(bugs_found)


 # 4 личный счетчик проверок
def make_counter():
  count = 0

  def next_check():
    nonlocal count
    count = count + 1
    return count

  return next_check


counter_a = make_counter()
counter_b = make_counter()
print(counter_a())  # 1
print(counter_a())  # 2
print(counter_b())  # 1
print(counter_a())  # 3
print(counter_b())  # 2

 # 5 баланс учебного буфета

def make_wallet(start_balance):
  balance = start_balance

  def buy(price):
    nonlocal balance

    if balance >= price:
      balance = balance - price
      return balance
    else:
      return -1

  return buy


ekeb_wallet = make_wallet(2000)
trip_wallet = make_wallet(500)

print(ekeb_wallet(700))
print(ekeb_wallet(1500))
print(ekeb_wallet(300))
print(ekeb_wallet(1000))
print(ekeb_wallet(1))
print(ekeb_wallet(0))
print(trip_wallet(200))

zero_wallet = make_wallet(0)

print(zero_wallet(0))
print(zero_wallet(1))




