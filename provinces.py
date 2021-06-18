def main():
    
    provinces = read_list("provinces.txt")
    
    print(provinces)

    provinces.pop(0)
    provinces.pop()

    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

    count = provinces.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")

def read_list(filename):
    text_lines = []

    with open("provinces.txt", "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_lines.append(clean_line)
    return text_lines        
        
if __name__ == "__main__":
    main()
    