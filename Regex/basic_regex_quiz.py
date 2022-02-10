import re

#checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters 
# (which includes letters, numbers, and underscores), 
# as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc.
def check_web_address(text):
  pattern = r"^[a-zA-Z0-9_][a-zA-Z0-9_\.\-\+]*[\.a-zA-Z]$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False


#checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon,
#  then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.
def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[am|pm|AM|PM]"
  result = re.search(pattern, text)
  return result != None

print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False


#checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter),
#returning True if the condition is met, or False otherwise. For example, 
#"Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions."
def contains_acronym(text):
  pattern = r"\([A-Z0-9][a-zA-Z0-9]*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False


# check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, 
# but not always, followed by a dash with 4 more digits.
# The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
def check_zip_code (text):
  result = re.search(r"[ ]\d{5}|[ ]\d{5}-\d{4}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False