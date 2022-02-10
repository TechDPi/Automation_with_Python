#Simple matching unsing rawstirng aza in a given string plaza

import re
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)

#usage of special character ^
print(re.search(r"^x", "xenon"))

#usage of special character .
print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))


# Function check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

#Ignore case sensitive

print(re.search(r"p.ng", "Penguin", re.IGNORECASE))