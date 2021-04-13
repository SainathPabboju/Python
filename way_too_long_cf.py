n = int(input())

for i in range(n):
    word = input()
    if len(word)>10:
        spabr = f"{word[0]}{len(word[1:-1])}{word[-1]}"
for i in range(n):
    if len(word)>10:
        spabr = f"{word[0]}{len(word[1:-1])}{word[-1]}"
        print(spabr)
    else:
        print(word)    