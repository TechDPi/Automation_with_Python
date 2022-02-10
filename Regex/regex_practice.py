import re

# All the word that start with A and finish with a
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbajan"))

# add char to specific the start of the line and end of the line
print(re.search(r"^A.*a$", "Argentina"))

# validating pattern for variable in python

pattern = r"^[a-zA-Z_][a-zA-z0-9_]*$"

print(re.search(pattern, "_this_is_valid"))

print(re.search(pattern, "_this is not valid"))
print(re.search(pattern, "9_this_not_valid"))

# check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space,
# and ends with a period, question mark, or exclamation point. 
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True