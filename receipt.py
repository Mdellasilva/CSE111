import csv

#CHECK TO SEE IF THE FORMAT OF THE DICTIONARY IS OKAY

PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1


def main():
    products = read_products("products.csv", 0)
    print("Products")
    
    for i in products:
            value = products[i]
            print(f"{i} {value}")
    
    print()

    print("Requested Items")
    process_request("request.csv", products)

def read_products(filename, key_column_index):
    product_dictionary = {}

    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        
        next(reader)

        for row in reader:
            key = row[key_column_index]

            product_dictionary[key] = [row[NAME_INDEX], row[PRICE_INDEX]]

    return product_dictionary

def process_request(filename, product_dictionary):
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            product = row[PRODUCT_INDEX]
            quantity = row[QUANTITY_INDEX]

            value = product_dictionary[product]
            name = value[0]
            price = value[1]

            print(f"{name}: {quantity} @ {price}")


if __name__ == "__main__":
    main()
