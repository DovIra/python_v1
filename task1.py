from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addUserDish(user_name, country, dish):

    if user_name in dataset:

        if country in dataset[user_name]:

            dish = dataset[user_name][country]
            country.append(dish)
        else:
            dataset[user_name][country] = [dish]
    else:
        dataset[user_name] = {country: {dish}}


print("Task 1")
addUserDish("EV346745", "Italian", "coca")

print(dataset)


print("\n\n")