
#print a look inside a log string using index 
#log = "12345678910 [123456789]"
#index = log.index("[")
#print(log[index+1:index+10])

# Use of regex and import re module
import re
log = "12345678910 [123456789]"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


