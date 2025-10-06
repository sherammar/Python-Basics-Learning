# ==============================
# 🧠 STRINGS & THEIR FUNCTIONS
# ==============================

# Q1: Create a string variable 'name' with your name and print its length using len().

# SOLUTION:

name = "    Ammar    Yasir    "
find_length = len(name)
print("Length of the Given String is: ", find_length)

# To remove any spaces from the string and find exact length

exact_length = len(name.strip().replace(" ", ""))
print("Exact number of characters: ", exact_length )





# Q2: Take a string "PYTHON" and convert it to lowercase using the appropriate function.

#SOLUTION:

language = "PYTHON"
lower_case = language.lower()
print("Converted String: ", lower_case)





# Q3: Remove extra spaces from the string "   Hello Python!   " and print the cleaned string.

# SOLUTION:

greet = "    Hello Python!      "
spaces_removed = greet.strip()
print("Clean String: ", spaces_removed)






# Q4: Replace the word "Java" with "Python" in the string "I love Java programming".

# SOLUTION:

string = "I love Java programming"
replaced_word = string.replace("Java", "Python")
print("Manipulated string: ", replaced_word)






# Q5: Split the string "apple,banana,orange" by commas and print the resulting list.

# SOLUTION:

string1 = "apple,banna,orrange"
new_list1 = string1.split(",")
print("List: ", new_list1)

# to verify it is a List, checking type

print(type(new_list1))








# Q6: Join the list ['Python', 'is', 'fun'] into a single string separated by spaces.

# SOLUTION:

list2 = ['Python', 'is', 'fun']
new_string = " ".join(list2)
print("Converted to string: ", new_string)

# to verify it is a List, checking type

print(type(new_string))




# Q7: Find the index of the word "world" in the string "Hello world, welcome to Python".

find_index = "Hello world, welcome to Python"
word_index = find_index.find("world")
print("Index numer: ", word_index)






# Q8: Count how many times the letter 'o' appears in "Hello, how are you doing?".

# SOLUTION:

sentence = "Hello, how are you doing?"
letter_counter = sentence.count("o")
print("Number of times the letter appeared: ", letter_counter)






# Q9: Given a string "data science", print it in uppercase and then lowercase.

term = "data science"
upper_case = term.upper()
print("In uppercase: ", upper_case)

print("Again in lower case: ", upper_case.lower())






# Q10: Write a program that takes user input and prints:
#       - The first character
#       - The last character
#       - The reversed string (using slicing)


# I will use a function for this challenge

# SOLUTION:

def string_manipulation(name):
    first_char = name[0]
    last_char = name[-1]
    reversed_string = name[::-1]
    return first_char, last_char, reversed_string   # when you return multiple values of function it by default returns a typle

user_input = input("Enter your name: ")

# calling the funtion and passing user_input as parameter

print(string_manipulation(user_input))






# ==============================
# 🧠 STRING SLICING PRACTICE
# ==============================

# Q1: Given the string "DataScience", print the following using slicing:
#     a) The first 4 characters
#     b) The last 3 characters
#     c) Every alternate character

# Example Output:
# First 4: Data
# Last 3: nce
# Alternate: DtScne

# SOLUTION:

string2 = "DataScience"
first_4_char = string2[:4]
last_3_char = string2[8:12]
alternate = string2[::2]
print(first_4_char)
print(last_3_char)
print(alternate)








# Q2: Given the string "PythonProgramming", use slicing to print:
#     a) The word "Python"
#     b) The word "Programming"
#     c) The reversed string

# Example Output:
# Python
# Programming
# reversed: gnimmargorPnohtyP

string3 = "PythonProgramming"
first_word = string3[:6]
second_word = string3[6:18]
reversed1 = string3[::-1]

print(first_word)
print(second_word)
print(reversed1)




# Q3: Take a string input from the user and:
#     a) Print only the middle portion (excluding the first and last 2 characters)
#     b) Print it backwards using slicing
#     c) Print every 2nd character

# Example Output (if user enters "KagglePython"):
# Middle: gglePyth
# Backwards: nohtyPelggagK
# Every 2nd char: KgePto

# SOLUTION:

complete_word = "KagglePython"
middle_portion = complete_word[2:-2]
backwards = complete_word[::-1]
every_2nd = complete_word[::2]

print(middle_portion)
print(backwards)
print(every_2nd)






