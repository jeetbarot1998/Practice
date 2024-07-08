def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if lengths are the same
    if len(word1) != len(word2):
        return False
    
    # Count frequency of each character
    count1 = {}
    count2 = {}
    
    for char in word1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
            
    for char in word2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
            
    # Compare character counts
    return count1 == count2

# Example usage:
word1 = "Listen"
word2 = "Silent"
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
