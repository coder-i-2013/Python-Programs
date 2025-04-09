class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi is widley spoken while there are many other languages")
    def type(self):
        print("India is a developing country")
class America():
    def capital(self):
        print("Washington DC")
    def language(self):
        print("Though there is no national language English is most commonly used")
    def type(self):
        print("America is a devoloped country")
obj_ind=India()
obj_usa=America()
for country in (obj_ind, obj_usa):
    country.capital()
    country.type()
    country.language()
