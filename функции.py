def check_case(function, value, expected):
    actual = function(value)
    return actual == expected


def eekb_price(price):
    if price >= 1000:
        return price - 100
    return price


print(check_case(eekb_price, 999, 999))
print(check_case(eekb_price, 1000, 900))
print(check_case(eekb_price, 1001, 901))
#ошибочная функция
def wrong_price(price):
    return price - 100


print(check_case(wrong_price, 999, 999))
print(check_case(wrong_price, 1000, 900))
print(check_case(wrong_price, 1001, 901))