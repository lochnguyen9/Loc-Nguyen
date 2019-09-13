#Loc Nguyen
#1001656113
#HW2

#1 A program that lets the salesman enter the quantity of each item sold, calculates the total sales, and prints as below.
for item_number in range(1,6):
    quantity = int(input("Enter quantity of item " + str(item_number) + " sold: "))
    if item_number == 1:
        price = 2.5
        sale_1 = price * quantity
        quantity_1 = quantity
    elif item_number == 2:
        price = 1.98
        sale_2 = price * quantity
        quantity_2 = quantity
    elif item_number == 3:
        price = 5.75
        sale_3 = price * quantity
        quantity_3 = quantity
    elif item_number == 4:
        price = 3.45
        sale_4 = price * quantity
        quantity_4 = quantity
    elif item_number == 5:
        price = 4
        sale_5 = price * quantity
        quantity_5 = quantity
total = sale_1 + sale_2 + sale_3 + sale_4 + sale_5
print('Item \t\t Quantity \t\tTotal')
print('-------------------------------------------------')
print(1,'\t\t',quantity_1,'\t\t\t$',format(sale_1,'5.2f'))
print(2,'\t\t',quantity_2,'\t\t\t$',format(sale_2,'5.2f'))
print(3,'\t\t',quantity_3,'\t\t\t$',format(sale_3,'5.2f'))
print(4,'\t\t',quantity_4,'\t\t\t$',format(sale_4,'5.2f'))
print(5,'\t\t',quantity_5,'\t\t\t$',format(sale_5,'5.2f'))
print()
print("The total of all sales is $", format(total,'5.2f'),sep = '')

#2 Develop #1 using a for loop to run for 3 salesmen and print the total sales for each salesman. 
for salesman_loop in range(1,4):
    name = input("Enter salemans name: ")
    for item_number in range(1,6):
        quantity = int(input("Enter quantity of item " + str(item_number) + " sold: "))
        if item_number == 1:
            price = 2.5
            sale_1 = price * quantity
            quantity_1 = quantity
        elif item_number == 2:
            price = 1.98
            sale_2 = price * quantity
            quantity_2 = quantity
        elif item_number == 3:
            price = 5.75
            sale_3 = price * quantity
            quantity_3 = quantity
        elif item_number == 4:
            price = 3.45
            sale_4 = price * quantity
            quantity_4 = quantity
        elif item_number == 5:
            price = 4
            sale_5 = price * quantity
            quantity_5 = quantity
    total = sale_1 + sale_2 + sale_3 + sale_4 + sale_5
    if salesman_loop == 1:
        hold_1 = total
        name_1 = name
    if salesman_loop == 2:
        hold_2 = total
        name_2 = name
    if salesman_loop == 3:
        hold_3 = total
        name_3 = name  
print("The total sales for " + name_1 + " is $", format(hold_1,'.2f'),sep = '')
print("The total sales for " + name_2 + " is $", format(hold_2,'.2f'),sep = '')
print("The total sales for " + name_3 + " is $", format(hold_3,'.2f'),sep = '')

#3 Develop #2 to let the salesman determine when he/she is finished entering the item/quantity.
for salesman_loop in range(1,4):
    name = input("Enter salemans name: ")
    item_number = int(input("Enter item number or -99 to quit: "))
    total = 0
    while item_number != -99:
        quantity = int(input("Enter quantity of item " + str(item_number) + " sold: "))
        if item_number == 1:
            price = 2.5
        elif item_number == 2:
             price = 1.98
        elif item_number == 3:
            price = 5.75
        elif item_number == 4:
            price = 3.45
        elif item_number == 5:
            price = 4
        sale = price * quantity
        total = total +sale 
        item_number = int(input("Enter item number: "))
    if salesman_loop == 1:
        hold_1 = total
        name_1 = name
    if salesman_loop == 2:
        hold_2 = total
        name_2 = name
    if salesman_loop == 3:
        hold_3 = total
        name_3 = name  
print("The total sales for " + name_1 + " is $", format(hold_1 ,'5.2f'),sep = '')
print("The total sales for " + name_2 + " is $", format(hold_2 ,'5.2f'),sep = '')
print("The total sales for " + name_3 + " is $", format(hold_3 ,'5.2f'),sep = '')
