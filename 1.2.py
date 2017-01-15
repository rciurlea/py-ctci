# Check Permutation: Given two strings, write a method
# to decide if one is a permutation of the other.

def is_perm(a, b):
    chars = {}
    for c in a:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c in b:
        if c in chars:
            chars[c] -= 1
        else:
            return False
    for c in chars:
        if chars[c] != 0:
            return False
    return True

print(is_perm("", ""))
print(is_perm("radu", "udar"))
print(is_perm("ana", "aan"))
print(is_perm("tttt", "tttt"))
print(is_perm("craci", "crac"))
print(is_perm("craci", "craca"))
