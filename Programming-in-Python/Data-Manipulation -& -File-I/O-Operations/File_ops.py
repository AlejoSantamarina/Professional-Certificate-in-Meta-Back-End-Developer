def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content
    
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        line = file.readlines()
    return line

def write_first_line_to_file(file_contents, output_filename):
    line = file_contents.split('\n')
    
    with open(output_filename, 'w') as file:
        file.write(line[0]) 


def read_even_numbered_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines[0::2] #Esto quiere decir lines[inicio:fin:paso]


def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    return lines[::-1] #Esto quiere decir que empieza desde el final de la lista (ya que no puse inicio) termina en el inicio de la lista y va decrementando de 1 en 1 en cada iteración.
    


# Sample commands to run/test your implementations.
def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()