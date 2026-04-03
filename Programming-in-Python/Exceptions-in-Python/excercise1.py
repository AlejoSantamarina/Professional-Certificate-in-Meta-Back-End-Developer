items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print("The index doesnt exist. Type of error:", e)

def divide_by(a, b):
    return a/b

try:
    ans = divide_by(40,0)
    print(ans)
except ZeroDivisionError as e:
    print("Division by zero is not allowed. Type of error: ", e)

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("The file could not be found. Type of error: ", e)