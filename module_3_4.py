def single_root_words(root_word, *other_words):
    same_words = []
    for i in list(other_words):
        if root_word.upper() in i.upper() or i.upper() in root_word.upper():
            same_words += [i]
    print(same_words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')