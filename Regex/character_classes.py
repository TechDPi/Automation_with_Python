import re

# Match word python wiht lower or uppercase P
print(re.search(r"[Pp]ython", "Python"))

#anyletter between range a-z before the given rawstring
print(re.search(r"[a-z]way", "The end of the highway"))

#space char doesent match the range a-z
print(re.search(r"[a-z]way", "What a way to go"))

# we can combine how many symbols we wants
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))


# function check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#search any character that is not a letter
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces"))

#search any character that is not a letter and spaces
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

#serch any 2 given string
print(re.search(r"cat|dog", "I like dogs"))

#serch both of 2 given string using findall function
print(re.findall(r"cat|dog", "I like dogs and cats"))