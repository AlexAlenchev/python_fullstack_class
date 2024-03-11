user_input = input("Введите строку: ")
try:
    number = int(user_input)
    result = str(number  *  2)
    print(result)
except ValueError:
    print("Введенная строка не может быть преобразована в число.")