minutes = input("Введите минуты: ")
print(
    minutes + " " + "мин" + " " + "-" + " " + "это" + " " f'{int(minutes) // int(60)}' + " " + "ч" + " " + f'{int(minutes) % int(60)}' + " " + "мин"
)

#Ввод:
#Введите минту: 785
#Вывод:
#785 мин - это 13 ч 5 мин