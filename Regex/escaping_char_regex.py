import re
from string import digits

#search dot in a string, and using \ character
print(re.search(r"\.com", "Welcom www.lol.com"))

#usage of \w, it match letter, number and underscores
print(re.search(r"\w*", "This is an example"))

#\d match digits
#\s match white spaces char

# the function check if the text passed has at least 2 groups of alphanumeric characters 
# (including letters, numbers, and underscores) separated by one or more whitespace characters.
def check_character_groups(text):
  result = re.search(r"(\w)+(\s)+(\w)+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False