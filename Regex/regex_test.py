import re

print(re.search(r"p.ng", "penguin"))

# check if aei occure in a given string
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None
