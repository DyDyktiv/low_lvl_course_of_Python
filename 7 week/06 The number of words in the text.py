import sys

words = set()
for s in sys.stdin:
    words.update(set(s.split()))
print(len(words))
