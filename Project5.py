def string_to_int(my_string, n):
    s = len(my_string) - n

    if s >= len(my_string) - 1:
        return 0
    while s < len(my_string) - 1:
        return ord(my_string[s]) + string_to_int(my_string, n - 1)


some_string = "Hello"

print(string_to_int(some_string, len(some_string)))
