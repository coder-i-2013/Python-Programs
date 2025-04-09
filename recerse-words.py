class ReverseLetters:
    def reverse(self, input_string):
        """Reverse the letters in the string."""
        return input_string[::-1]
word= input("Pick the name you want to reverse:  ")
reverser = ReverseLetters()
print(reverser.reverse(word))  
