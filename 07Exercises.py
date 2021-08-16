# 7.11. Exercises: Strings
line_start = "<--------------"
line_end = "-------------->"
'''

# 7.11.1. Part One: Bracket Notation
print(f"\n{line_start} PART 1 {line_end}")
# 1. Identify the result for each of the following statements:
print("'Characters'[8] will result in 'r'")
print('"Strings are sequences of characters."[5] will result in "g"')
print('len("Wonderful") will result in 9')
print('len("Do spaces count?") will result in 16')
'''

# Use bracket notation to:
    # 2a. Print a slice of the first 12 characters from "Strings_are_sequences_of_characters."
    # 2b. Print a slice of the last 12 characters from the same string. 
        # You should NOT have to count the index values yourself!
    # 2c. Print a slice of the middle 12 characters from the same string.
string_one = "Strings_are_sequences_of_characters."
print(f'\nThe full string being used is: {string_one}')
print(f'The slice of the first 12 characters is: {string_one[:12]}')
print(f'The slice of the last 12 characters is: {string_one[-12:]}')
middle_index = len(string_one)//2
print(f'The slice of the middle 12 characters is: {string_one[(middle_index - 6):(middle_index + 6)]}')

# Use index values to loop backwards through a string:
    # 3a. First, print one letter per line.
    # 3b. Next, instead of one letter per line, use the accumulator pattern to build up and 
        # print the reversed string. 
        # For example, if given the string 'good', your program prints doog.
    # 3c. Finally, use concatenation to print the combination of the original and reversed string. 
        # For example, given the string 'tomato', your program prints tomatootamot. 
        # (If you want to be fancy, include the | character to make the output look almost like 
        # a mirrored image: tomato | otamot).

print('\nLooping backwards\n')
string_two = 'Coding'
for index in range(len(string_two)):
    backward = -1 - index
    print(string_two[backward])

string_three = ''

# 7.11.2. Part Two: String Methods and Operations
print(f"\n{line_start} PART 2 {line_end}")
#

# 7.11.3. Part Three: String Formatting
print(f"\n{line_start} PART 3 {line_end}")
# 