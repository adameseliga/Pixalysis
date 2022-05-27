my_string = "It is not me, but it is a me."


def char_occurrence(some_string):
    for c in some_string:
        if (c.lower() or c.upper()) not in some_string[some_string.index(c)+1:]:
            return c


print(char_occurrence(my_string))
