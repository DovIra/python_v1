from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.
#паспорт: дві великі літери англійської абетки у верхньому регістрі, потім 6 цифр.
#назва країни та страви : не більше 10 літер англійської абетки у нижньому регістрі, перша літера завжди велика


from validators.lib import getUserPassport
from validators.lib import getCountryName
from validators.lib import getDishName




from task1 import addUserDish


#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserDishValidator():

    user_input = getUserPassport()
    while not user_input:
        print("Error in number of passport. Try again")
        user_input = getUserPassport()

    country = getCountryName()
    while not country:
        print("Error in name of country. Try again")
        country = getCountryName()

    dish = getDishName()
    while not dish:
        print("Error in name of dish. Try again")
        dish = getDishName()

    addUserDish(user_input,country , dish)



print("Task 1")
addUserDishValidator()
print(dataset)


print("\n\n")