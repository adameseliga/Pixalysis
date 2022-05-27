my_string = "It is not me, but it is a me."


def char_occurrence(some_char,some_string):
    my_table = {}

    for c in my_string:
        if c not in my_table:
            my_table[c.lower()] = 1
        else:
            my_table[c] += 1

    return my_table[some_char]


print(char_occurrence('i', my_string))
