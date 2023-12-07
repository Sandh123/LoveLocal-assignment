def shortest_palindrome(s):
    if not s:
        return ""

    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    if i == len(s):
        return s

    suffix = s[i:]
    prefix = suffix[::-1]
    mid = shortest_palindrome(s[:i])
    
    return prefix + mid + suffix
user_input = input()
result = shortest_palindrome(user_input)
print("Shortest palindrome:", result)
