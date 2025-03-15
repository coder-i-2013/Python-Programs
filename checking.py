def contains_A(string):
    for char in string:
        if char == 'A':
            print("Alphabet 'A' found in the string!")
            break
    else:
        print("Alphabet 'A' not found in the string.")
    for char in string:
        if char == 'a':
            print("Alphabet 'A' found in the string!")
            break
    else:
        print("Alphabet 'A' not found in the string.")

# Example usage
check_word = input("Enter a word: ") 
contains_A(check_word)