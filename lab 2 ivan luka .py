users = {
    "ivan": ["1234", [10, 8, 4, 12, 3, 9, 7]],
    "petro": ["qwerty", [5, 6, 2, 4, 11, 12, 1]],
    "olga": ["pass123", [12, 11, 10, 9, 8, 7, 6]],
    "max": ["0000", [2, 3, 4, 1, 3, 4]]
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login][0] == password:
    grades = users[login][1]

    good_grades = 0
    bad_grades = 0

    for g in grades:
        if g >= 5 and g <= 12:
            good_grades += 1
        elif g >= 1 and g <= 4:
            bad_grades += 1

    print("\nАвторизація успішна!")
    print("Ваші оцінки:", grades)
    print("Задовільних оцінок (5-12):", good_grades)
    print("Незадовільних оцінок (1-4):", bad_grades)
else:
    print("\nНевірний логін або пароль!")