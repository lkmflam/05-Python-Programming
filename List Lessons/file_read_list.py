# This program reads a file's contents into a list

def main():
    # Open a file for reading
    infile = open('cities.txt', 'r')

    # Read the contents of the file into a list
    cities_read_in = infile.readlines()

    # Close the file
    infile.close()

    # Strip the \n from each element
    index = 0
    while index < len(cities_read_in):
        cities_read_in[index] = cities_read_in[index].rstrip('\n')
        index += 1

    # Print the contents of the list
    print(cities_read_in)

# Call the main function
main()