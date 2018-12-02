student = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for s in f:
        s = s.split()
        s.pop(2)
        student.append(s)
student.sort(key=lambda st: st[0])
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(map(lambda st: ' '.join(st), student)))
