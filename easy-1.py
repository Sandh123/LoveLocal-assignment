def length(s):
    words = s.split()
    if len(words) > 0:
        return len(words[-1])
    else:
        return 0
input_string = input()
result = length(input_string)
print(result)
