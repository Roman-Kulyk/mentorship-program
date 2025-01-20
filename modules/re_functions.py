import re


# 1. re.findall() - returns all non-overlapping matches of pattern in string,
# as list of strings.

# string = """Hello my number is 123456789 and
#             my friend's number is 987654321"""
# regex = '\d+'
# match = re.findall(regex, string)
# print(match)

# # 2. re.compile() - regular expressions are compiled into pattern objects,
# # which have methods for various operations such as searching for pattern
# # matches or performing string substitutions.
# p = re.compile('[a-e]')
# print(p.findall("Aye, said Mr. Giberson Stark"))

# p = re.compile('\d')  # It finds single digits
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# p = re.compile('\d+')  # It finds sequences of digits
# print(p.findall("I wetn to him at 11 A.M. on 4th July 1886"))

# p = re.compile('\w')
# print(p.findall("He said * in some_lang."))

# p = re.compile('\w+')
# print(p.findall("I went to him at 11 A.M., he\
#                 said *** in some_language."))

# p = re.compile('\W')
# print(p.findall("he said *** in some_language."))

# p = re.compile('ab*')
# print(p.findall("ababbaabbb"))

# # 3. re.split() - split string by the occurrences of a character or a pattern,
# # upon finding that pattern, the remaining characters from the string are
# # returned as part of the resulting list.
# from re import split
# print(split('\W+', 'Words, words, Words'))
# print(split('\W+', "Word's words Words"))
# print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
# print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

# # Splits the string at the first occurence of one or more digits
# print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# # Splits the string using lowercase letters a to f as delimiters, case-insensitive
# print(re.split('[a-f]', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))

# # Splits the string using lowercase letters a to f as delimiters, case-sensitive
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))

# # 4.re.sub()
# # The 'sub' in the function stands for SubString, a certain regular expression
# # pattern is searched in the given string, and upon finding the substring pattern
# # is replaced by repl

# print(re.sub('ub','~*', 'Subject has Uber booked already',
#              flags=re.IGNORECASE))
# print(re.sub('ub','~*', 'Subject has Uber booked already'))
# print(re.sub('ub','~*', 'Subject has Uber booked already',
#              count=1, flags=re.IGNORECASE))
# print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
#              flags=re.IGNORECASE))

# # 5. re.subn()
# # subn() is similar to sub() in all ways, except in its way of providing output.
# # It returns a tuple with a count of the total of replacement and new string
# # rather than just the string.

# print(re.subn('ub', '~*', 'Subject has Uber booked already'))
# t = re.subn('ub', '~*', 'Subject has Uber booked already',
#             flags=re.IGNORECASE)
# print(t)
# print(len(t))
# print(t[0])

# # 6. re.escape()
# # Returns string with all non-alphanumerics backslashed, this is useful if you
# # want to match an arbitrary literal string that may have regular expression
# # metacharacters in it.
# print(re.escape("This is Awesome even 1 AM"))
# print(re.escape("I Asked what is this [a - 9], he said \t ^WoW"))

# 7. re.search()
# This method either returns None (if the pattern doesn't match), or
# a re.MatchObject contain information about the matching part of the string.

regex = r"([a-zA-Z]) (\d+)"

match = re.search(regex, "I was born on June 24")
if match != None:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
else:
    print("The regex pattern does not match.")