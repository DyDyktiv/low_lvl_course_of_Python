n = int(input())
requireds = set(input() for i in range(int(input())))
languages = requireds.copy()
for schoolboy in range(n - 1):
    schoolboy_languages = set(input() for i in range(int(input())))
    requireds.intersection_update(schoolboy_languages)
    languages.update(schoolboy_languages)
print(len(requireds), '\n'.join(requireds), sep='\n')
print(len(languages), '\n'.join(languages), sep='\n')
