from datetime import datetime

current = datetime.now()
weekday = current.isoweekday()

#weekday will hold 1 if today is Monday, 2 if today is Tuesday, and so on to 7 if today is Sunday

#finish = input('Enter done when finished. ')

finish = ''
while finish.lower() != 'done':
    price = float(input('What is the price of the product? '))
    quantity = int(input('How many would you like to purchase? '))
    subtotal = price * quantity
    finish = input('Is that all? (Continue/Done).: ')
    #subtotal = float(input('What is the subtotal? '))
    if subtotal >= 50 and (weekday == 2 or weekday == 3):
        discount = subtotal * .10
        print(f'The discount is ${discount:.2f}')
        subtotal = subtotal - discount
        sales_tax = subtotal * 0.06
        print(f'The sales tax is ${sales_tax:.2f}')
        total_after_tax = subtotal + sales_tax
        print(f'Your total is ${total_after_tax:.2f}')
    else:
        sales_tax = subtotal * 0.06
        print(f'The sales tax is ${sales_tax:.2f}')
        total_after_tax = subtotal + sales_tax
        print(f'Your total is ${total_after_tax:.2f}')

    if subtotal <= 50 and (weekday == 2 or weekday == 3):
        additional_amount = 50 - subtotal
        print(f'The amount you need to purchase to get the discount is ${additional_amount:.2f}')
        
        
        #additional_amount = 50 - subtotal
        #print(f'The amount you need to purchase to get the discount is ${additional_amount:.2f}')
    