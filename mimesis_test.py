from mimesis import Person
from mimesis.enums import Gender

'''
Reminder this is a drinks-ordering application. What behaviour can be randomly generated

'''

# de = Person('de')
en = Person('en')

print(en.full_name(gender=Gender.MALE))
print(en.full_name(gender=Gender.FEMALE))

list_en_names = []

for i in range(10):
    list_en_names[i] = en.full_name(gender=Gender.MALE)



'''
Create fake-data generator
- data should be each in a line,

'''