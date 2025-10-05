# ============================================================
# 🧩 PART 1: Basic Function Structure
# ============================================================

# ------------------------------------------------------------
# No Parameter, No Return
# ------------------------------------------------------------

# Write a function that simply prints "Welcome to Python!".

# def greet():
#     print("Welcome to Python!")

# greet()

# Question to think: What happens if you try to use the function’s output in another expression?
# I think i can use it like this:

# def another_function():
#     greet()

# another_function()


# ------------------------------------------------------------
# Parameter, No Return
# ------------------------------------------------------------

# Write a function print_double(num) that prints double of a number.

# def print_double(num):
#     num += num
#     print("Double: ", num)

# print_double(10)
# print_double(10.5)

# Try calling it with both integer and float values — what do you observe?
# I observed that it is perfectly working for both int and float.


# ------------------------------------------------------------
# Parameter, With Return
# ------------------------------------------------------------

# Write a function get_double(num) that returns double of a number.

# def get_double(num):
#     num += num
#     return num

# print(get_double(20))
# print(get_double(20.5))

# How is this different from printing inside the function?
# It is different in a way that when we don’t use print inside the function,
# we have to use print with calling the function to get the value.


# ------------------------------------------------------------
# 🧠 Challenge: describe_double()
# ------------------------------------------------------------

# Write a function describe_double(num) that returns a formatted string,
# like "The double of 4.5 is 9.0".

# def describe_double(num):
#     double_of_num = num * 2
#     return f"The double of {num} is {double_of_num}"

# print(describe_double(4.5))


# ============================================================
# 🧩 FUNCTION EXERCISES
# ============================================================

# ------------------------------------------------------------
# 🔹 1. String Play — "Mirror Me"
# ------------------------------------------------------------

# Write a function mirror_text(text) that returns a string saying:
# "The mirror of hello is olleh"

# 🪞 Hint: Think of how you reversed text earlier with slicing ([::-1]).

# def mirror_text(text):
#     mirror = text[::-1]
#     return f"The mirror of {text} is {mirror}"

# print(mirror_text("hello"))


# ------------------------------------------------------------
# 🔹 2. Boolean Logic — "The Truth Teller"
# ------------------------------------------------------------

# Write a function truth_teller(statement) that returns
# "True Statement!" if the argument is True, and "False Alarm!" otherwise.

# 💭 Hint: You’ll pass in a boolean (True or False) and return a sentence based on it.

# def truth_teller(statement):
#     if statement:
#         return "True Statement!"
#     else:
#         return "False Alarm!"

# print(truth_teller(False))


# ------------------------------------------------------------
# 🔹 3. Int & Conditionals — "Grade Genius"
# ------------------------------------------------------------

# Write a function grade_message(marks) that:
# Returns "Excellent" if marks ≥ 80
# Returns "Good" if marks are between 50 and 79
# Returns "Try Again" otherwise

# 💡 Hint: This is a perfect example for multiple conditionals.

# def grade_message(marks):
#     if marks >= 80:
#         return "Excellent"
#     elif 50 < marks <= 79:
#         return "Good"
#     else:
#         return "Try Again"

# remarks = grade_message(80)
# print("Remarks upon your marks:", remarks)


# ------------------------------------------------------------
# 🔹 4. Float & Comparison — "Weight Check"
# ------------------------------------------------------------

# Write a function compare_weight(w1, w2) that:
# Takes two weights (floats)
# Returns "w1 is heavier", "w2 is heavier", or "Both are equal"

# 🥇 Hint: Focus on conditional structure and formatted strings.

# def compare_weight(w1, w2):
#     if w1 > w2:
#         return f"{w1} is heavier"
#     elif w2 > w1:
#         return f"{w2} is heavier"
#     else:
#         return "Both are equal"

# comparison = compare_weight(5.45, 49.04)
# print(comparison)


# ------------------------------------------------------------
# 🔹 5. Combined Logic — "Magic Name"
# ------------------------------------------------------------

# Write a function magic_name(name) that:
# Removes extra spaces
# Converts it to lowercase
# Returns True only if the name is "python" or "ammar"

# 🧙‍♂️ Hint: Combine .strip(), .lower(), and a boolean or.

# def magic_name(name):
#     name = name.strip().lower()
#     if name == "python" or name == "ammar":
#         return True
#     else:
#         return False

# result = magic_name("amar")
# print(result)


# ------------------------------------------------------------
# 🔹 6. User Input Challenge — "Simple Calculator"
# ------------------------------------------------------------

# Write a function simple_calculator() that:
# Asks the user for two numbers (ints or floats)
# Returns their sum, difference, product, and quotient

# Format: "Sum: 10, Difference: 4, Product: 21, Quotient: 2.33"

# def simple_calculator():
#     input1 = float(input("Number 1: "))
#     input2 = float(input("Number 2: "))
#     sum1 = input1 + input2
#     difference = input1 - input2
#     product = input1 * input2
#     quotient = input1 / input2
#     return f"Sum: {sum1}, Difference: {difference}, Product: {product}, Quotient: {quotient}"

# result = simple_calculator()
# print(result)


# ------------------------------------------------------------
# 🔹 7. String & Boolean Combo — "Starts with P?"
# ------------------------------------------------------------

# Write a function starts_with_p(word) that:
# Returns True if the given word starts with “p” (case-insensitive), otherwise False.

# def starts_with_p(word):
#     word1 = word.lower()
#     if word1[0] == "p":
#         return True
#     else:
#         return False

# result = starts_with_p("Pakistan")
# print(result)


# ------------------------------------------------------------
# 🔹 8. Logical Reasoning — "Odd or Divisible"
# ------------------------------------------------------------

# Write a function odd_or_divisible(num) that:
# Returns True if the number is odd or divisible by 5, else False.

# def odd_or_divisible(num):
#     if num % 2 != 0 or num % 5 == 0:
#         return True
#     else:
#         return False

# result = odd_or_divisible(22)
# print(result)


# ------------------------------------------------------------
# 🔹 9. Input + Return — "Double or Triple"
# ------------------------------------------------------------

# Write a function double_or_triple() that:
# Takes a number input from the user
# If number > 10 → return its double
# Otherwise → return its triple

# def double_or_triple():
#     num = int(input("Number: "))
#     if num > 10:
#         return num * 2
#     else:
#         return num * 3

# result = double_or_triple()
# print(result)


# ------------------------------------------------------------
# 🔹 10. Smart String — "Word Length Judge"
# ------------------------------------------------------------

# Write a function judge_length(word) that:
# Returns "Short" if len ≤ 4, "Medium" if 5–8, "Long" otherwise.

# def judge_length(word):
#     if len(word) <= 4:
#         return "Short"
#     elif len(word) >= 5 and len(word) <= 8:
#         return "Medium"
#     else:
#         return "Greater"

# result = judge_length("ammar")
# print(result)


# ============================================================
# 🧩 TYPE CONVERSIONS AND LOGIC
# ============================================================

# ------------------------------------------------------------
# 🔹 11. String → Int — "Age in 5 Years"
# ------------------------------------------------------------

# Write a function future_age() that:
# Asks user to enter age (string), converts to int, and returns age + 5.

# def future_age():
#     age = int(input("Enter your age: ")) + 5
#     return f"Your age after 5 years is {age}"

# find_age_after5 = future_age()
# print(find_age_after5)


# ------------------------------------------------------------
# 🔹 12. Float → Int — "Rounded Price"
# ------------------------------------------------------------

# Write a function rounded_price(price) that:
# Takes a float and returns it as an integer (rounded down).

# def rounded_price(price):
#     return int(price)

# result = float(input("Enter the floating number: "))
# print(rounded_price(result))


# ------------------------------------------------------------
# 🔹 13. Int → Float — "Area in Meters"
# ------------------------------------------------------------

# Write a function to_square_meters(area) that:
# Takes an integer in cm², converts it to m² (divide by 10000), and returns float.

# def to_square_meters(area):
#     return float(area) / 10000

# print(to_square_meters(100))


# ------------------------------------------------------------
# 🔹 14. String → Bool — "Is It Yes?"
# ------------------------------------------------------------

# Write a function is_yes(answer) that:
# Returns True if input string (case-insensitive) is "yes", else False.

# def is_yes(answer):
#     if answer.lower() == "yes":
#         return True
#     else:
#         return False

# print(is_yes("No"))


# ------------------------------------------------------------
# 🔹 15. Combined Conversion — "Bill Calculator"
# ------------------------------------------------------------

# Write a function calculate_bill() that:
# Asks user for item_price and quantity (float), returns total cost.

# Example: price = "25.5", quantity = "2" → total = 51.0

# def calculate_bill():
#     item_price = float(input("What is the price of item? "))
#     quantity = float(input("How many items you had? "))
#     return item_price * quantity

# total_price = calculate_bill()
# print("Your Bill is:", total_price)