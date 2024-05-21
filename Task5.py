def is_palindrome(s):
    s = s.lower()
    
    # Remove non-alphanumeric characters from the string
    s = ''.join(char for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
