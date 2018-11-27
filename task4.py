from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки страв полюбляє.

data = ?

diagram = ?

fig = ?

plotly.offline.plot(?)

from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.

data = dict()
for user_input in list (dataset.keys()):
    for dish, dish_list in ( dataset[user_input]).items():
        if user_input in data:
            data[user_input] += sum(dish_list)
        else:
            data[user_input] = sum(dish_list)

print(data)

diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
