import csv

INUM_INDEX = 0
NAME_INDEX = 1


def main():
    
    # read_dictionary("students.csv")
    # check_ID(Id)

    dictionary = read_dictionary("students.csv", INUM_INDEX)
  
    Id = str(input("Enter ID: "))
   
    
    if Id in dictionary:
        value = dictionary[Id]
        name = value[NAME_INDEX]
        print(name)
        
    else:
        print("No such student")


def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            key = row[key_column_index]

            dictionary[key] = row

    return dictionary




if __name__ == "__main__":
    main()