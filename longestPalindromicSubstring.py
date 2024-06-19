def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    # Table to store results of subproblems.
    storeResult = [[False] * n for _ in range(n)]
    # All substrings of length 1 are palindromes.
    start = 0
    max_length = 1
    for i in range(n):
        storeResult[i][i] = True
    # Check for sub-string of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            storeResult[i][i + 1] = True
            start = i
            max_length = 2
    # Check for lengths greater than 2 and here k is length of substring.
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if storeResult[i + 1][j - 1] and s[i] == s[j]:
                storeResult[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    req_substring = s[start:start + max_length]
    return req_substring

input_string = input("Enter a string: ")
result = longest_palindromic_substring(input_string)
print("The longest palindromic substring is :", result, "and its length is :", len(result))