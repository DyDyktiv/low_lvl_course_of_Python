name = dict()
vote = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        if line in name:
            name[line] += 1
        else:
            name[line] = 1
        vote += 1
sort = sorted(name, key=lambda x: name[x], reverse=True)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(sort[0])
    if name[sort[0]] <= vote / 2:
        f.write(f'\n{sort[1]}')
