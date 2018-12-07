words = dict()
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            words[word] = words.get(word, 0) + 1
table = sorted(words, reverse=True, key=lambda x: words[x])
equalwords = 1
for word in table[1:]:
    if words[table[0]] == words[word]:
        equalwords += 1
    else:
        break
print(sorted(table[: equalwords])[0])
