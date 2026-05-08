#opening a file
try:
    with open('text.txt', mode = 'r') as file:
        data = file.readlines()

        print(data)
except FileNotFoundError as e:
    print(f"The file is not found. Type of error:{e}")

#write-only to the file, replacing it each time

with open('newfile.txt', 'w') as file:
    file.write("This is a new file created.")

#write only to the file, without replacing it each time

with open('newfile.txt', 'a') as file:
    file.write("This is a new file created.")

#types of reading

with open('Programming-in-Python/Python-file-handling/test.txt', 'r') as file:
    print(file.read(10))
    print(file.read())

    file.seek(0)
    print(file.readline())
    print(file.readlines())