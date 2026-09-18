def vowel(n):
    c=0
    for i in n:
        if i.lower().startswith(("a", "e", "i", "o", "u")):
            c=c+1
    return c