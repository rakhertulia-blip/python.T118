def entry_message(group):
    if group == "Т118":
        return "Т118: вход разрешён"
    else:
        return "Обратитесь к куратору"

check_entry = entry_message


result1 = check_entry("Т118")
result2 = check_entry("Т119")
result3 = check_entry("т118")
result4 = check_entry("")

print(type(check_entry))
print(type(result1))
