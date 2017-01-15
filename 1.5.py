# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two
# strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def one_edit_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) > len(b):
        a, b = b, a
    ia = ib = mismatches = 0
    while ia < len(a):
        if a[ia] != b[ib]:
            if mismatches > 0:
                return False
            mismatches += 1
            if len(a) < len(b):
                ib += 1
            else:
                ia += 1
                ib += 1
        else:
            ia += 1
            ib += 1
    return True

print(one_edit_away("pale", "ple"))
print(one_edit_away("pales", "pale"))
print(one_edit_away("pale", "bale"))
print(one_edit_away("pale", "bake"))
