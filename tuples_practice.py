# ==============================
# 🧠 PYTHON TUPLES PRACTICE
# ==============================

# Q1: Create a tuple with 5 numbers and print:
#     a) The first and last elements
#     b) The length of the tuple
#     c) The tuple in reverse order

# Solution:

five_elements = (40, 50, 60, 70, 80)
first = five_elements[0]
second = five_elements[-1]
find_length = len(five_elements)
backwards = five_elements[::-1]

print("Original tuple's data: ", five_elements)
print("First and last element: ", first)
print("Second and last element: ", second)
print("Length: ", find_length)
print("Reversed tuple: ", backwards)







# Q2: Create a tuple with mixed data types (string, int, float, boolean).
#     Print each element on a new line using a loop.

# SOLUTION:

mixed_types = ("Ammar", 24, 182.6, True)
for mix in mixed_types:
    print(mix)







# Q3: Create a tuple (10, 20, 30, 40, 50)
#     a) Print the element at index 2
#     b) Slice and print elements from index 1 to 3


# Solution:

new_tuple = (10, 20, 30, 40, 50)
index_2 = new_tuple[2]
sliced_tuple = new_tuple[1:4]

print("Element at index 2: ", index_2)
print("Sliced tuple: : ", sliced_tuple)



# Q4: Given the tuple (2, 4, 6, 8, 10, 4, 4)
#     a) Count how many times 4 appears
#     b) Find the index of first occurrence of 8

given_tuple = (2, 4, 6, 8, 10, 4, 4)
count_appearances = given_tuple.count(4)
first_appearance = given_tuple.index(8)

print("Total Occurences of 4: ", count_appearances)
print("First occurence of 8 is at index: ", first_appearance)







# Q5: Write a program that takes a tuple of numbers and prints the maximum and minimum values.
#     (Hint: use max() and min() functions)

# Solution:

user_input = tuple(map(int, input("Enter the numbers: ").split()))
max_value = max(user_input)             # we cannot use max or min function as user_input.max(), because it is a funtion not a method
min_value = min(user_input)

print("Max value in the tuple is: ", max_value)
print("Min value in the tuple is: ", min_value)





# Q6: Create a nested tuple ((1, 2, 3), (4, 5, 6))
#     Access the element ‘5’ using indexing.


# Solution:

nested_tuple = ((1,2,3), (4,5,6))
element_index = nested_tuple[1][1]
print("Accessing element 5: ", element_index)



