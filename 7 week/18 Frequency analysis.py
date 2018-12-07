words = dict()
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            words[word] = words.get(word, 0) + 1
sort = dict()
for word in words:
    if sort.get(words[word], False):
        sort[words[word]].append(word)
    else:
        sort[words[word]] = [word]
for value in sorted(sort, reverse=True):
    for word in sorted(sort[value]):
        print(word)
