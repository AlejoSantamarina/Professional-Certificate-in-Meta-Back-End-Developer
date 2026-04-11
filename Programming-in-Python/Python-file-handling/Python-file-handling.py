#opening a file
try:
    with open('text.txt', mode = 'r') as file:
        data = file.readlines()

        print(data)
except FileNotFoundError as e:
    print(f"The file is not found. Type of error:{e}")

#write-only to the file, replacing it each time

with open('newfile.txt', 'a') as file:
    file.write("This is a new file created.")

#write only to the file, without replacing it each time
