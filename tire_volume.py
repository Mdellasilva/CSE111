import math
from datetime import datetime

current_date = datetime.now()

run = input('Do you want to shop for some tires? (yes/no) ')
while run.lower() != 'no':
    tire_width = float(input('Enter the width of the tire in mm (ex 205): '))
    aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
    wheel_diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

    print()

    volume = (math.pi * (tire_width ** 2) * aspect_ratio * (tire_width * aspect_ratio + (2540 * wheel_diameter))) / 10000000

    print(f'The approximate volume is {volume:.1f} milliliters')

    purchase = input('Do you want to buy the tires with these dimensions? (yes/no) ')

    with open('volumes.txt', 'at') as volumes_file:
        print(f'{current_date}, {tire_width:.0f}, {aspect_ratio:.0f}, {wheel_diameter:.0f}, {volume:.1f}', file=volumes_file)
    
    if purchase.lower() == 'yes':
        name = input('What is your name? ')
        phone_number = input('What is your phone number? ')
        with open('volumes.txt', 'at') as volumes_file:
            print(f'Name: {name} Phone Number: {phone_number}', file=volumes_file)

    print()

    run = input('Do you want to shop for more tires? (yes/no) ')