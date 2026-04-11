#opening a file
try:
    with open('text.txt', mode = 'r') as file:
        data = file.readlines()

        print(data)
except FileNotFoundError as e:
    print(f"The file is not found. Type of error:{e}")

#file creation

with open('newfile.txt', 'w') as file:
    file.write("This is a new file created.")