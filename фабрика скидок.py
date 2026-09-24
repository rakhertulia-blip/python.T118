def make_discount(amount):
    def discount(price):
        result = price - amount

        if result < 0:
            result = 0

        return result

    return discount


discount_100 = make_discount(100)
discount_300 = make_discount(300)

print(discount_100(250))
print(discount_300(250))
print(discount_100(100))
print(discount_100(0))
print(discount_300(500))
print(discount_100(500))

discount_0 = make_discount(0)

print(discount_0(500))

print(discount_100(99))
print(discount_100(101))