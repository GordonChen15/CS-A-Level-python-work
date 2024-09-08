# Wite a program in python that takes in an input string containing text and single digit non negative integers which can replace all the numbers in the input with their text equivalents.
# Answer extracted from ChatGPT
# Create a dictionary to map digits to their text equivalents
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

# Read input string from user
input_string = input("Enter a string with text and single-digit numbers: ")

# Initialize an empty result string
result_string = ""

# Loop over the input string and replace digits with words
for i in range(len(input_string)):
    char = input_string[i]
    # Check if the character is a digit
    if char in digit_to_word:
        # Replace digit with corresponding word
        result_string += digit_to_word[char]
    else:
        # If it's not a digit, keep the character as is
        result_string += char

# Print the final result
print(result_string)
