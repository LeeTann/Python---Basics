student = {'name': 'John', 'age': 25, 'course': ['Math', 'CompSci']}

print(student) # {'name': 'John', 'age': 25, 'course': ['Math', 'CompSci']}
print(student['name']) # John
# print(student['phone']) ## KeyError: 'phone' - when trying to get a key no in dict
print(student.get('phone')) # get() returns None instead of Error

student['name'] = 'Jane'
print(student) # {'name': 'Jane', 'age': 25, 'course': ['Math', 'CompSci']}

student.update({'name': 'Lee', 'age': 39, 'phone': '555-5555'}) # update() great for updating multpile keys/values 
print(student) # {'name': 'Lee', 'age': 39, 'course': ['Math', 'CompSci'], 'phone': '555-5555'}

del student['age']
print(student) # {'name': 'Lee', 'course': ['Math', 'CompSci'], 'phone': '555-5555'}

popped_phone = student.pop('phone')
print(popped_phone) # 555-5555
print(student) # {'name': 'Lee', 'course': ['Math', 'CompSci']}

print(len(student)) # print length of keys in student which is 2 - 'name' and 'course'
print(student.keys()) # dict_keys(['name', 'course'])
print(student.values()) # dict_values(['Lee', ['Math', 'CompSci']])
print(student.items()) # dict_items([('name', 'Lee'), ('course', ['Math', 'CompSci'])])

for key, value in student.items():
  print(key, value)

print(student['course'][0]) # Math