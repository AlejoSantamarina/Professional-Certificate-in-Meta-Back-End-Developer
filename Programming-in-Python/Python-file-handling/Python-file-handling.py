try:
    with open('text.txt', mode = 'r') as file:
        data = file.readlines()

        print(data)
except FileNotFoundError as e:
    print(f"The file is not found. Type of error:{e}")