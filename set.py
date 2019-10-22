## Sets are very useful since they can't have duplicates
courses = {'History', 'Math', 'Physics', 'CompSci'}
courses_2 = {'History', 'Math','Art', 'Design' }

print(courses) # {'CompSci', 'History', 'Math', 'Physics'}
print(courses.intersection(courses_2)) # {'Math', 'History'}
print(courses.difference(courses_2)) # {'Physics', 'CompSci'}
print(courses.union(courses_2)) # {'Math', 'Design', 'History', 'Physics', 'Art', 'CompSci'}

# Empty List
empty_list = []
empty_list = ()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} ## This isnt right! It's a dictionary
empty_set = set() # for empty set, you have to use the built in method set()