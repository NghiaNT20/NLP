# How to extract usernames from emails ?
'''Extract the usernames from the email addresses present in the text

Input :

text= "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly contact granger111@gamil.com or severus77@gamil.com "
Desired Output :

['potter709', 'elixir101', 'granger111', 'severus77']'''

import re
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 

text= "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly contact granger111@gamil.com or severus77@gamil.com "
usernames = re.findall('(\S+)@', text)
print(usernames)