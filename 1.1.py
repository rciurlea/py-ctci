# Is Unique: Implement an algorithm to determine if a string has
# all unique characters. What if you cannot use additional data structures?

def unique_chars(s):
    chars = {}
    for c in s:
        if c in chars:
            return False
        else:
            chars[c] = True
    return True

print(unique_chars(""))
print(unique_chars("a"))
print(unique_chars("ana"))
print(unique_chars("radu"))
print(unique_chars("ra ra rasputin"))
