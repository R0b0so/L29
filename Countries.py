class India():
    def capital(self):
        print("New Delhi is India's capital")
    def language(self):
        print("Hindi is India's language")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington DC is USA's capital")
    def language(self):
        print("English is USA's language")
    def type(self):
        print("USA is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()