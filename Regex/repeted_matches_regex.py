import re
#usage of .* - greedy
print(re.search(r"Py.*n", "I like Python"))

print(re.search(r"Py.*n", "Python Programming"))

#less greedy, consider only letters range a-z
print(re.search(r"Py[a-z]*n", "Python Programming"))

#+ char
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
# + char but doesnet match
print(re.search(r"o+l+", "boil"))

#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
#For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.
def repeating_letter_a(text):
  result = re.search(r"[aA]+(.*)+[aA]+", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# ? char usage, in this following example the char p is optional
print(re.search(r"p?each", "To each of their own"))

print(re.search(r"p?each", "I like peaches"))

