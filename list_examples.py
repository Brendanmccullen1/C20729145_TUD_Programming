#course: Object-oriented programming, year 2, semester 1
#academic year: 2021-22
#author: B. Schoen-Phelan
#date: 11-10-2021
#purpose: List examples

names = ['Bianca', 'Brian', 'Susan']
numbers = [1,2,3]
num = 5

# add a list to a list
# names.extend(numbers)
names.append(numbers)
# print(names)

# add one item to a list
# names.append(num)
# names.extend(num)

# print(names)






to_sort = ['x', 'a', 'f', 'x']
# print(sorted(to_sort)) # ['a', 'f', 'x', 'x']
# print(to_sort) # ['x', 'a', 'f', 'x']
to_sort.sort()
print(to_sort)

original = ['a', 'b', 'c']
# copy = original
# print(copy) # ['a', 'b', 'c']
# print(original) # ['a', 'b', 'c']
#
# copy.extend([1,2,3])
# print(copy) # ['a', 'b', 'c', 1, 2, 3]
# print(original) # ['a', 'b', 'c', 1, 2, 3]
#
# print(id(copy))
# print(id(original)) # have same location

# create a true copy
copy = original.copy()
# print(copy) # ['a', 'b', 'c']
# print(original) # ['a', 'b', 'c']
copy.extend([1,2,3])
# print(copy) # ['a', 'b', 'c', 1, 2, 3]
# print(original) # ['a', 'b', 'c']

# print(id(copy))
# print(id(original)) # have different location


# alternatives
copy = original[:] # use slice notation
copy2 = list(original) # list function

# print(copy)
# print(copy2)
copy.extend([1,2,3])
copy2.extend(['x', 'y', 'z'])
# print(copy) # ['a', 'b', 'c', 1, 2, 3]
# print(copy2) # ['a', 'b', 'c', 'x', 'y', 'z']
# print(original) # ['a', 'b', 'c']






# to_sort.sort() #no return value
# print(to_sort)
# to compare try
# to_sort = to_sort.sort()
# print(to_sort) # returns None
