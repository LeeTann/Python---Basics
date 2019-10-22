courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Education', 'Geography']
nums = [1, 5, 2, 4, 3]
nums_2 = [7, 10, 6, 9, 8]

print(courses[0:2]) # start at index 0 and end at index 2. ['History', 'Math']
                    # start is inclusive, end is exclusive.
print(courses[:2]) # slicing - ['History', 'Math']
print(courses[2:]) # slicing - ['Physics', 'CompSci']
print(courses[-1]) # get last item - CompSci

### Methods for List

courses.append('Art')
print(courses) # ['History', 'Math', 'Physics', 'CompSci', 'Art']

courses.insert(0, 'P.E.')
print(courses) # ['P.E.', 'History', 'Math', 'Physics', 'CompSci', 'Art']

courses.extend(courses_2)
print(courses) # ['P.E.', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education', 'Geography']

courses.remove('Math')
print(courses) # ['P.E.', 'History', 'Physics', 'CompSci', 'Art', 'Education', 'Geography']

popped = courses.pop()
print(popped) # removes last item - Geography

courses.reverse()
print(courses) # ['Education', 'Art', 'CompSci', 'Physics', 'History', 'P.E.']

courses.sort()
print(courses) # ['Art', 'CompSci', 'Education', 'History', 'P.E.', 'Physics']

nums.sort(reverse=True)
print(nums) # [5, 4, 3, 2, 1]

sorted_nums_2 = sorted(nums_2) # sorted() does not alter original list
print(nums_2) # [7, 10, 6, 9, 8]
print(sorted_nums_2) # [6, 7, 8, 9, 10]

print(min(nums)) # 1
print(max(nums)) # 5
print(sum(nums)) # 15

### print each item 
for course in courses:
  print(course)

for index, course in enumerate(courses): # enumerate returns the index and value
  print(index, course)

# converion to string
course_string = ' - '.join(courses) # convert list into a string
print(course_string) # Art - CompSci - Education - History - P.E. - Physics

new_list = course_string.split(' - ') # converts back to a list
print(new_list) # ['Art', 'CompSci', 'Education', 'History', 'P.E.', 'Physics']
