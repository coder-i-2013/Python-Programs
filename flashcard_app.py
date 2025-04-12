class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        
        return self.word +'('+self.meaning+')'

flash=[]
print("Welcome to Flashcard Application") 
while(True):
    word=input("Enter the word you would like to create a flascard of: ")
    meaning=input("Enter the meaning or definition of the word")
    flash.append(Flashcard(word,meaning))
    option= int(input("Enter 0 if you want to create another card \nEnter 1 if you are done creating cards: "))
    if(option):
            break
print("\n Your Flashcards")  
for i in flash: 
    print(">",i)
