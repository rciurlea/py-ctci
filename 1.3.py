# URLify: Write a method to replace all spaces in a string with '%20:.
# You may assume that the string has sufficient space at the end to
# hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use
# a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# Probably not what we want :D
# def URLify_stlib(s):
#     return "%20".join(s.split(" "))
#
# print(URLify_stlib("Mr John Smith"))

def URLify(chars, length):
    offset = len(chars) - length
    i = len(chars) - 1
    while i - offset >= 0:
        if chars[i - offset] != " ":
            chars[i] = chars[i - offset]
            i -= 1
        else:
            chars[i] = "0"
            chars[i-1] = "2"
            chars[i-2] = "%"
            i -= 3
            offset -= 2

def mkList(s):
    l = []
    spaces = 0
    for c in s:
        l.append(c)
        if c == ' ':
            spaces += 1
    l = l + spaces * 2 * [' ']
    return (l, len(s))

array, length = mkList("Mr John Smith")
URLify(array, length)
print(array)
