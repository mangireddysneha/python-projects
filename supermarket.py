import math
from datetime import datetime

a = input("Enter your name: ")
items = []
price = 0
totalprice = 0
list = {
    'rice': 70,
    'sugar': 100,
    'salt': 40,
    'oil': 60,
    'dal': 80,
    'milk': 50,
    'pens': 10,
    'books': 25
}

while True:
    print('''
         1.list of items
         2.choose a item
         3.exit      ''')

    choice = int(input())
    if choice == 1:
        print(list)
    if choice == 2:
        b = input("enter the item name:")
        items.append(b)
    if choice == 3:
        print("exit the process")
        break

print("-------------- BILL -------------")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Customer Name:", a)
print("Date & Time  :", dt_string)
print("--------------------------")
print("Items added to cart:")
for item in items:
    print(f" {item}: ₹{list.get(item)}")
    totalprice += list.get(item)
print("--------------------------")
print("Total Amount: ₹", totalprice)
print("--------------------------")