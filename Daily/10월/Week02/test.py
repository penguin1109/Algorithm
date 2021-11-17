import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    else:
        words = []
        for _ in range(n):
            w = (str(input()).strip())
            words.append(w)
        words.sort(key = lambda w:w.lower())
        print(words[0])