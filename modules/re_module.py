import re

s = 'geeks.forgeeks'

# METACHARACTERS
# 1. \-Backslash
# The basckslash (\) makes sure that the character is not treated in a special
# way. This can be considered a way of escapint metacharacters.

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)

# 2. []-Square Brackets
# Square Brackets ([]) represetn a character class consisting of a set of 
# characters that we with to match.

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-e]"
result = re.findall(pattern, string)
print(result)

# 3. ^-Caret
# Caret(^) symbol matches the beginning of the string i.e. checks whether the
# string starts with the given character(s) or not.

regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')

# 4. $-Dollar
# Dollar ($) symbol matches the end of the string i.e checks whether the string
# ends with the given character(s) or not.

string = "Hello World!"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

# 5..-Dot
# Dot(.) symbol matches only a single character except for the newline
# character(\n)

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

# 6.|-Or
# Or(|) symbol works as the operator meaning it cheeks whether the pattern
# before or after or symbol is present in the string or not.

# 7.?-Question Mark
# The question mare(?) symbol is a quantifier in regular expressions that the
# preceding element shoud be matched zero on one time.

# 8.*-Star
# Star symbol(*) matches zero or more occurences of regex preceding the * symbol.

# 9.+-Plus
# Plus(+) symbol matches one or more occurences of the regex preceding the +
# symbol

# {m,n}-Group
# Braces {} match any repetitions preceding regex from m to n both inclusive.