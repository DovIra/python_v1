"""
    Написати валідатор ....
    Правило валідації
"""

import re


def getUserPassport():
    user_input = input("введить номер вашого закордонного паспорту")
    if (re.match(r"^[A-Z]{2}\d{6}$", user_input)):
        return user_input
    else:
        return False

def getCountryName():
    country = input("введіть назву країни")
    if (re.match(r"^[A-Z]{1}[a-z]{0,10}$", country)):
        return country
    else:
        return False

def getDishName():
    dish = input("введіть назву страви")
    if (re.match(r"^[A-Z]{1}[a-z]{0,10}$", dish)):
        return dish
    else:
        return False

