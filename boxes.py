import math

number_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))
number_of_boxes = math.ceil(number_items / items_per_box)

#This is code to use if you don't use the math.ceil function
#extra_items = number_items % items_per_box
#if extra_items >= 1:
#   number_of_boxes = (number_items // items_per_box) + 1
#else: number_of_boxes = number_items // items_per_box

print(f'For {number_items} items, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.')