
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02}

time = [my_favorite_songs_dict['Waste a Moment'],
        my_favorite_songs_dict['New Salvation'],
        my_favorite_songs_dict['Staying\' Alive'],
        my_favorite_songs_dict['Out of Touch'],
        my_favorite_songs_dict['A Sorta Fairytale'],
        my_favorite_songs_dict['Easy'],
        my_favorite_songs_dict['Beautiful Day'],
        my_favorite_songs_dict['Nowhere to Run'],
        my_favorite_songs_dict['In This World']]

# присвоила переменной time список продолжительностей песен из словаря my_favorite_songs_dict

import random
x=random.sample(time, 3)

# присвоила переменной x 3 произвольных времени из списка time

y1,y2,y3 = int(x[0]),int(x[1]),int(x[2])
z1,z2,z3 = round((x[0]-int(x[0]))*100),round((x[1]-int(x[1]))*100),round((x[2]-int(x[2]))*100)

# присвоила переменным y1-y3 значения минут каждой песни из списка x
# присвоила переменным z1-z3 значения секунд каждой песни из списка x

import datetime
time1 = datetime.timedelta(0,z1,0,0,y1)
time2 = datetime.timedelta(0,z2,0,0,y2)
time3 = datetime.timedelta(0,z3,0,0,y3)
time = time1 + time2 + time3

# перевела время каждой песни в формат времени datatime
# сложила время всех песен

print("Три песни звучат",time, "минут")