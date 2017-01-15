# Palindrome Permutation: Given a string, write a function to check if it is
# a permutation of a palindrome. A palindrome is a word or phrase that is
# the same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

def is_palindrome_perm(s):
    chars = {}
    for c in s:
        if c == ' ':
            continue
        cl = c.lower()
        if cl in chars:
            chars[cl] += 1
        else:
            chars[cl] = 1
    odd_found = False
    for c in chars:
        if chars[c] % 2 == 1:
            if odd_found:
                return False
            odd_found = True
    return True

print(is_palindrome_perm("aannbbcd"))
