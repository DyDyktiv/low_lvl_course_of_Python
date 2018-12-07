words = dict()
result = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            r = words.get(word, 0)
            result.append(r)
            words[word] = r + 1
print(*result)
