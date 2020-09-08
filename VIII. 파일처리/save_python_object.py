#230

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def __str__(self):
        return f'이름 : {self.name}\n나이 : {self.age}'

p = Person('김수현', '010-2222-3333')

file = open('person_data.bin', 'wb')
pickle.dump(p, file)
file.close()