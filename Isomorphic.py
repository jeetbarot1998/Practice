""" Isomorphic strings are strings in which characters in one string can be replaced to get the other string, maintaining the order of characters. For two strings to be isomorphic, there must be a one-to-one mapping between characters in the first string and characters in the second string.
Problem Statement
Given two strings s and t, determine if they are isomorphic.

Example
vbnet
Copy code
Input: s = "egg", t = "add"
Output: True

Input: s = "foo", t = "bar"
Output: False

Input: s = "paper", t = "title"
Output: True
Explanation
"egg" and "add":

'e' maps to 'a'
'g' maps to 'd'
Every occurrence of 'e' can be replaced with 'a' and 'g' with 'd' to get "add". Therefore, they are isomorphic.
"foo" and "bar":

'f' maps to 'b'
'o' maps to 'a'
But 'o' cannot map to 'a' and 'r' at the same time. Therefore, they are not isomorphic.
"paper" and "title":

'p' maps to 't'
'a' maps to 'i'
'p' maps to 't' again (consistent mapping)
'e' maps to 'l'
'r' maps to 'e'
All characters map consistently, so they are isomorphic. """

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Dictionaries to store the mapping of characters from s to t and t to s
    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for char_s, char_t in zip(s, t):
        # Check the mapping from s to t
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t

        # Check the mapping from t to s
        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s

    return True

# Examples
print(isIsomorphic("egg", "add"))  # Output: True
print(isIsomorphic("foo", "bar"))  # Output: False
print(isIsomorphic("paper", "title"))  # Output: True
