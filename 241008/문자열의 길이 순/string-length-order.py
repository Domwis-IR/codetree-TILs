n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append((len(word), word))

words.sort(key=lambda words: words[0])

for num, word in words:
    print(word)