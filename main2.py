
#Task2
# #Mastering Python Modules and Aliases
#Task 1: Custom Module with Aliases
#Problem Statement: Create a custom module named `text_utils.py`
# with functions for string manipulation (e.g., reversing a string, capitalizing).
# In your main script, import this module using an alias and utilize its functions.
  # text_utils.py


import text_utils
def main():
  while True:

    word=input("Please type a word or sentense: ")
    reverse=input('Would you like to reverse the word or capitalize the word: ').lower()
    if reverse==("reverse"):
      print(text_utils.reverse_string(word))
    elif reverse==("capitalize"):
      print(text_utils.capitalize_string(word))
    else:
      print("Please enter 'reverse' or 'capitalize'")
main()