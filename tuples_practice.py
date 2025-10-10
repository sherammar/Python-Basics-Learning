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



# More Practice Questions for tuples




# ==============================
# 🧠 ADVANCED TUPLE PRACTICE
# ==============================

# Q1: Create two tuples:
#     tuple1 = (1, 2, 3)
#     tuple2 = (4, 5, 6)
#     Concatenate them into a new tuple and print the result.

#Solution:

tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple is: ", concatenated_tuple)







# Q2: Repeat the tuple (7, 8) three times using the repetition operator (*)
#     and print the resulting tuple.

#Solution:

tuple_repeat = (7,8)
print("Three times repeated tuple: ", tuple_repeat * 3)






# Q3: Given tuple = (10, 20, 30, 40, 50)
#     a) Slice and print the last three elements.
#     b) Slice and print every second element.

#Solution:

given_tuple = (10,20,30,40,50)
sliced_tuple1 = given_tuple[2:5]
print("Last Three elements" ,sliced_tuple1)
sliced_and_print_every2nd = given_tuple[::2]
print("Accessing Every 2nd element: ", sliced_and_print_every2nd)








# Q4: Create a nested tuple:
#     nested = (('a', 'b', 'c'), (1, 2, 3), ('x', 'y', 'z'))
#     a) Access the element 'y'
#     b) Access the element 3

#Solution:

nested = (('a', 'b', 'c'), (1, 2, 3), ('x', 'y', 'z'))
access_element_y = nested[2][1]
access_element_3 = nested[1][2]
print("Element Y accessed: ", access_element_y)
print("Element 3 accessed: ", access_element_3)







# Q5: Create two tuples: (1, 2, 3) and ('a', 'b', 'c')
#     Combine them into one tuple of pairs like:
#     ((1, 'a'), (2, 'b'), (3, 'c'))
#     (Hint: Use the zip() function)

# Solution:

num_tuple = (1,2,3)
char_tuple = ('a','b','c')
combined_tuple = tuple(zip(num_tuple,char_tuple))

print("Combined tuple with pairs: ", combined_tuple)






# Q6: Given a tuple (10, 20, 30, 40, 50)
#     Unpack the values into separate variables and print each variable.

#Solution:

Q6_tuple = (10, 20, 30, 40, 50)

# Unpacking
a, b, c, d, e = Q6_tuple

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)






# Q7: Check if the element 25 exists in the tuple (10, 20, 30, 40)
#     Print a message accordingly using if-else.

#Solution: 

Q7_tuple = (10,20,30,40)

if 25 in Q7_tuple:
    print("Element Found!")
else:
    print("Element Not Found!")







# Q8: Create a tuple of strings:
#     colors = ('red', 'blue', 'green', 'yellow')
#     Convert it into a single comma-separated string using join().

#Solution:

colors = ('red', 'blue', 'green', 'yellow')
converted_colors = ",".join(colors)
print("Colors in string: ", converted_colors)






# Q9: Given the nested tuple:
#     data = (('Alice', 25, 'F'), ('Bob', 30, 'M'), ('Eve', 22, 'F'))
#     a) Print the name and age of the second person.
#     b) Print the gender of the last person.

#Solution:

data = (('Alice', 25, 'F'), ('Bob', 30, 'M'), ('Eve', 22, 'F'))
name_2ndperson = data[1][0]
age_2ndperson = data[1][1]
print(name_2ndperson, age_2ndperson)

gender_lastperson = data[2][2]
print(gender_lastperson)






# Q10: Write a program to find the sum of all elements in the tuple (5, 10, 15, 20, 25)
#      without using loops directly.
#      (Hint: Use the built-in sum() function)





#Solution:

Q10_tuple = (5, 10, 15, 20, 25)
sum_of_Q10 = sum(Q10_tuple)
print(sum_of_Q10)




