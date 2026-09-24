def student_info(name , age , city = "не указан"):
    return f"ученик: {name} , возраст : {age} , город: {city}"
print(student_info("Арман" , 16 , "Кызылорда"))
print(student_info("Alisher",18,))
print(student_info("Als",11))