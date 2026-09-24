def standard_fare(km):
    return 500 + 100 * km


def student_fare(km):
    return 300 + 70 * km


def trip_cost(km, tariff):
    return tariff(km)


print(trip_cost(10, standard_fare))
print(trip_cost(10, student_fare))

print(trip_cost(0, standard_fare))
print(trip_cost(0, student_fare))

print(trip_cost(1, standard_fare))
print(trip_cost(1, student_fare))
