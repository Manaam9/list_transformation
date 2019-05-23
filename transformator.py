def transform(list):
    """
    This function converts I/P list is : ['aaabbbbccdee'] into O/P is: a3b4c2de2.
    It gets a list and returns a string.

    aaaa = a3
    bbbb = b4
    cc = c2
    d = d ( here we do not write d1 . )
    ee = e2
    """

    # counting letters in our string inside list
    c = {}
    for i in list[0]:
        c[i] = c.get(i, 0) + 1

    # using generator to generate a string, iterating with cycle "for" thru key and value in our c dict
    # method "join" concatenates our key and value method
    # dict method items() retuns key and value pairs to handle with cycle "for"
    q = ''.join(key + str(value) for key, value in c.items())
    q = q.replace("1", "")
    return q
