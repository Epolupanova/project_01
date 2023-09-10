
titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

x = [
    titles['Кроссовки тип 3 (Adidas)'],
     titles['Мячик тип 2 (Adidas)'],
     titles['Кепка тип 1 (Adidas)'],
     titles['Ремень тип 2 (Nike)'],
     titles['Футболка тип 1 (Adidas)'],
     titles['Шапка тип 5 (Puma)']
    ]

# присвоила переменной x список из элементов словаря titles (кодов), соответствующих названиям товаров

y1,y2,y3,y4,y5,y6 = store[x[0]],store[x[1]],store[x[2]],store[x[3]],store[x[4]],store[x[5]]

# присвоила переменным y1-y6 списки из словаря store, соответсвующих ключам (кодам)

z1,z6 = y1[0],y6[0]
z21,z22 = y2[0],y2[1]
z31,z32 = y3[0],y3[1]
z41,z42 = y4[0],y4[1]
z51,z52,z53 = y5[0],y5[1],y5[2]

# присвоила переменным z словари из списков переменных y1-y6

a1,a6 = z1['quantity'],z6['quantity']
a2 = z21['quantity'] + z22['quantity']
a3 = z31['quantity'] + z32['quantity']
a4 = z41['quantity'] + z42['quantity']
a5 = z51['quantity'] + z52['quantity'] + z53['quantity']

# присвоила переменным а значения количества товаров по каждой позиции

b1,b6 = a1*z1['price'],a6*z6['price']
b2 = z21['quantity']*z21['price'] + z22['quantity']*z22['price']
b3 = z31['quantity']*z31['price'] + z32['quantity']*z32['price']
b4 = z41['quantity']*z41['price'] + z42['quantity']*z42['price']
b5 = z51['quantity']*z51['price'] + z52['quantity']*z52['price'] + z53['quantity']*z53['price']

# присвоила переменным b значения общей стоимости товаров по каждой позиции

print('Кроссовки тип 3 (Adidas) -',a1,'шт,  стоимость',b1,'руб.')
print('Мячик тип 2 (Adidas)     -',a2,'шт,  стоимость',b2,'руб.')
print('Кепка тип 1 (Adidas)     -',a3,'шт,  стоимость',b3,'руб.')
print('Ремень тип 2 (Nike)      -',a4,'шт,   стоимость',b4,'руб.')
print('Футболка тип 1 (Adidas)  -',a5,'шт, стоимость',b5,'руб.')
print('Шапка тип 5 (Puma)       -',a6,'шт,  стоимость',b6,'руб.')