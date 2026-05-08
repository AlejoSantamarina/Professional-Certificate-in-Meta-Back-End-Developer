def read_file(file_name):
    with open('/home/alejosantamarina/Developer/Professional-Certificate-in-Meta-Back-End-Developer/Programming-in-Python/Data-Manipulation -& -File-I/sampletext.txt', 'r') as file:
        print(file.read())
    
def read_file_into_list(file_name):
    with open('/home/alejosantamarina/Developer/Professional-Certificate-in-Meta-Back-End-Developer/Programming-in-Python/Data-Manipulation -& -File-I/sampletext.txt', 'r') as file:
        list = file.readlines()
        print(list)

def write_first_line_to_file(file_contents, output_filename):
    line = file_contents.split('\n')
    
    with open(output_filename, 'w') as file:
        file.write(line[0]) 


def read_even_numbered_lines(file_name):
    """ Reads even-numbered lines of a file and returns them as a list.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and add the even-numbered lines to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of even-numbered lines in the file (2, 4, 6, etc.).
    """
    ### WRITE SOLUTION HERE
    


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of its lines in reverse order.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and store the lines in a list in reverse order.
        3. Print the list.
        4. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of lines from the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    


# Sample commands to run/test your implementations.
def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "output.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
