import random
from random import randint

names = ["Jack", "Utkirbek", "Lili","Lolo", "Alis"]

dict_names = {student: random.randint(1,100) for student in names}
print(dict_names)

passed_students = {student:score for (student, score) in dict_names.items() if score > 50}
print(passed_students)