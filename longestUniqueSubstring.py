#This problem deals with the longest substring without repeating characters.
def length_of_longest_substring(s):
    try:
        char_map = {} #This is an empty dictionary to keep track of the most recent index of each character.
        left = 0
        max_length = 0
        start = 0 # Starting index of the longest substring.

        for right in range(len(s)):
            if s[right] in char_map:
                left = max(char_map[s[right]] + 1, left)
            char_map[s[right]] = right
            if max_length < right - left + 1:
                max_length = right - left + 1
                start = left

        longest_substring = s[start:start + max_length]
        return max_length, longest_substring
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, ""

s = input("Enter any string : ")
length, substring = length_of_longest_substring(s)
print(f"Length of longest unique substring: {length}")
print(f"Longest unique substring: '{substring}'")