# This program demonstrates the insert method

def main():
    # Create a list with some names
    names = ['James', 'Kathryn', 'Bill']

    # Display the list
    print('This list before insert:')
    print(names)

    # Insert a new name at element 0
    names.insert(0, 'Joe')

    # Display the list again
    print('The list after insert: ')
    print(names)

# Call the main function
main()