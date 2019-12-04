# This program uses the write method and a for loop to save
# a list of strings to a file

def main():
    # Create a list of strings
    cities = ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']

    # Open a file for writing
    outfile = open('cities2.txt', 'w')

    # Write the list to the file
    for item in cities:
        outfile.write(item)

    # Close the file
    outfile.close()

# Call the main function
main()


