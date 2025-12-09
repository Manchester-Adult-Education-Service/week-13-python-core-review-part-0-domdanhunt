# -------------------------------------------
# Exercise 0: Core Python Revision
# -------------------------------------------
# This exercise is designed to help you revise the fundamental concepts of Python
# covered in the course, preparing you for future modules and projects.
#
# Key Concepts to practise:
# - Variable Initialisation and Scope
# - Arithmetic and Comparison Operators
# - User Input (input(), int(), str())
# - Conditionals (if, elif, else)
# - Loops (for, while)
# - Lists and Dictionaries (Data Structures)
# - Basic Function Definition
#
# -------------------------------------------
# INDIVIDUAL INSTRUCTIONS
# -------------------------------------------
# Work independently on these tasks.
# If you get stuck on a concept, please check your notes first, and then ask a
# fellow student for assistance. Use your teacher only as a final resort—this is
# a great opportunity to practise working things out collaboratively!
# -------------------------------------------


# -------------------------------------------
# Task 1: Variables, Arithmetic, and Output
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Variables, Arithmetic, and Output\n"
    + "-------------------------------------------")

# TODO:
# 1. Initialise a variable called 'price' and set it to 45.00.
# 2. Initialise a constant variable called 'VAT_RATE' and set it to 0.20 (20%).
# 3. Calculate the 'total_cost' (price plus VAT).
# 4. Print the final 'total_cost' using an f-string, formatted to two decimal places.

# Write your code below:
price = 45.00
VAT_RATE = 0.20
total_cost = (price*VAT_RATE)
print(f"{total_cost:.2f}")
# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. The output should show the total cost as £54.00.
# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run the following Git steps:
#    Stage your changes
#    Commit your changes with a meaningful message
#    Push your changes
# -------------------------------------------


# -------------------------------------------
# Task 2: Conditionals (IF/ELIF/ELSE) and Comparison
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Conditionals (IF/ELIF/ELSE) and Comparison\n"
    + "-------------------------------------------")

# TODO:
# 1. Initialise a variable 'budget' and set it to 50.
# 2. Use an **IF/ELIF/ELSE** block to compare 'total_cost' (from Task 1) to 'budget'.
# 3. If 'total_cost' is less than or equal to 'budget', print "Purchase approved: Within budget."
# 4. If 'total_cost' is greater than 'budget' but less than 60, print "Warning: Purchase exceeds budget but is manageable."
# 5. Otherwise (if total_cost is 60 or more), print "Purchase denied: Budget severely exceeded."

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. Which message is printed? Try changing the 'price' in Task 1 to see the other messages.
# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run the following Git steps:
#    Stage your changes
#    Commit your changes with a meaningful message
#    Push your changes
# -------------------------------------------


# -------------------------------------------
# Task 3: Debugging a Function (Fixing a Crash)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Debugging a Function (Fixing a Crash)\n"
    + "-------------------------------------------")

# The function below is supposed to calculate the area of a rectangle,
# but it will crash if the user enters non-numerical data (e.g. 'five').
#
# TODO:
# 1. **Debug** the `calculate_area` function by adding **try/except** logic
#    to prevent a `ValueError` if the user enters text instead of a number.
# 2. If a `ValueError` occurs, the function should print "Error: Please enter only numerical values." and return 0.
#
# HINT: You may need to use a single `try` block that covers both `int()` conversions.

def calculate_area():
    # Insert try/except block here
    # Remember to handle the input() and int() conversions inside the try block
    length = int(input("Enter rectangle length: "))
    width = int(input("Enter rectangle width: "))
    area = length * width
    return area
    # Insert except block here

# Call the function:
rectangle_area = calculate_area()
print(f"Calculated Area: {rectangle_area}")


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. Enter '5' for length and '10' for width (result 50).
# Then, run it again and enter 'five' for length (result should be 0, and no crash).
# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run the following Git steps:
#    Stage your changes
#    Commit your changes with a meaningful message
#    Push your changes
# -------------------------------------------


# -------------------------------------------
# Task 4: Lists and the FOR Loop
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 4: Lists and the FOR Loop\n"
    + "-------------------------------------------")

# A list of weekly sales figures (in pounds):
weekly_sales = [120.50, 155.75, 95.00, 180.25, 130.50]

# TODO:
# 1. Initialise a variable called 'total_sales' and set it to 0.
# 2. Use a **FOR loop** to iterate through the `weekly_sales` list.
# 3. Inside the loop, add each sale amount to 'total_sales'.
# 4. Calculate the 'average_sale' (total_sales divided by the number of days).
# 5. Print both the 'total_sales' and 'average_sale', formatted to two decimal places.

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. Total Sales should be £682.00.
# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run the following Git steps:
#    Stage your changes
#    Commit your changes with a meaningful message
#    Push your changes
# -------------------------------------------


# -------------------------------------------
# Task 5: Dictionaries and Data Lookup
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 5: Dictionaries and Data Lookup\n"
    + "-------------------------------------------")

# A small dictionary containing product codes and their prices:
product_catalogue = {
    'PRD001': 15.99,
    'PRD002': 22.50,
    'PRD003': 8.75,
    'PRD004': 40.00
}

# TODO:
# 1. Ask the user to input a product code (e.g. 'PRD002').
# 2. Use an **IF/ELSE** check to see if the code exists as a **key** in the `product_catalogue`.
# 3. If the code exists, print the product code and its price (formatted to two decimal places).
# 4. If the code does not exist, print "Error: Product code not found."

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your program. Test with 'PRD004' and then test with a non-existent code like 'PRD005'.
# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run the following Git steps:
#    Stage your changes
#    Commit your changes with a meaningful message
#    Push your changes
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# If you have completed the main tasks, try these extensions to
# really test your skills!
# -------------------------------------------

# Extension 1: Input Validation for String/Number
# -------------------------------------------
# The code in Task 5 will crash if the product code is not in the correct format.
#
# TODO:
# 1. Modify the input prompt in Task 5 to ensure the user's input is always converted to uppercase (to match the keys).
# 2. **Optional but Recommended:** Review the solution provided by the tutor for handling `ValueError` (like in Task 3) and apply that knowledge to Task 5 to prevent potential crashes if the dictionary used different data types.

# -------------------------------------------

# Extension 2: The WHILE Loop Challenge
# -------------------------------------------
# Create a small program that asks the user to guess a secret colour.
#
# TODO:
# 1. Initialise a variable 'secret_colour' (e.g. "BLUE").
# 2. Use a **WHILE loop** to continuously ask the user for their guess.
# 3. If the guess is correct (ignoring case), print "You guessed it!" and use `break` to exit the loop.
# 4. If the guess is wrong, print "Try again."

# Write your code below:
print("\n-------------------------------------------\n"
    + "Extension 2: The WHILE Loop Challenge\n"
    + "-------------------------------------------")

# Write your code below:


# -------------------------------------------

# Extension 3: List Manipulation
# -------------------------------------------
# We need to filter a list of numbers to find only the even ones.
#
# TODO:
# 1. Initialise an empty list called 'even_numbers'.
# 2. Use a **FOR loop** to check each number in the list `data_set`.
# 3. Use the modulo operator (`%`) to check if a number is even (remainder is 0).
# 4. If it's even, use the `.append()` method to add it to 'even_numbers'.
# 5. Print the final 'even_numbers' list.

# Write your code below:
print("\n-------------------------------------------\n"
    + "Extension 3: List Manipulation\n"
    + "-------------------------------------------")

data_set = [3, 12, 5, 8, 17, 24, 9, 10]
even_numbers = []

# Write your code below:


# -------------------------------------------
# ADVANCED ACTIVITY: Combining Concepts
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: Combining Concepts\n"
    + "-------------------------------------------")

# TODO:
# 1. Define a function `process_order(order_dict, catalogue)` that takes a dictionary (the user's order) and the `product_catalogue` dictionary (from Task 5) as arguments.
# 2. The `order_dict` contains product codes and quantities: {'PRD001': 2, 'PRD003': 5}.
# 3. Inside the function, use a **FOR loop** to iterate through the items in `order_dict`.
# 4. For each product code, look up its price in the `catalogue`.
# 5. Calculate the subtotal for that item (price * quantity).
# 6. Return the **Grand Total** for the entire order.

# Write your code below:
def process_order(order_dict, catalogue):
    grand_total = 0
    print("--- Processing Order ---")
    # Insert code to loop through the order and calculate the total here
    return grand_total

# Test the function:
user_order = {
    'PRD001': 2,
    'PRD003': 5,
    'PRD099': 1
}

# Call the function and print the final bill (formatted to two decimal places):
# Write your code below:


# -------------------------------------------
# FINAL CHECKPOINT
# -------------------------------------------
# Verify your Advanced Activity calculates the correct total (75.73) and prints the warnings.
# -------------------------------------------
# SUBMITTING YOUR WORK
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes.
# 2. Commit with an appropriate message (e.g. "Completed Exercise 0 Revision").
# 3. Push your final version to the repository.
# -------------------------------------------
