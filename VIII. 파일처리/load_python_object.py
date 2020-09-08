#247

import pickle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'이름 : {self.name}\n나이 : {self.age}'

p = Person('김미림', 18)
p2 = Person('이미림', 20)
p3 = Person('최미림', 34)
people = [p, p2, p3]

# print(people)
# for person in people:
#     print(person)

file = open('person_data.bin', 'rb')
person = pickle.load(file)
file.close()

# print(person)
# print(person.name)
# print(person.age)


with open('people_data.bin', 'rb') as file:
    p_list = pickle.load(file)

print(p_list)
for p in p_list:
    print(p)