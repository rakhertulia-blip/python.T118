def calculate_discount(price,discount=0):
    return price - (price * discount/100)
print (calculate_discount(1000 , 15))

