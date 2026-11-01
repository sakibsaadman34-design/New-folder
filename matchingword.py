def match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("The words that match the first letter and the last letters are", lst)
    return ctr

count = match(["abc", "cfc", 'xyz', 'aba', '1221'])
print("The matching words in the list are", count)