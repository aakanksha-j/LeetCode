# follow up from isomorphic strings and find and replace pattern

# group isomorphic strings

# using tuple as key for dictionary and returning dictionary values as a list

def groupIsomorphic(words):
    word_dic = {}
    for word in words:
        key = tuple([word.find(ch) for ch in word])
        print(key)
        word_dic[key] = word_dic.get(key, []) + [word]

    return list(word_dic.values())
