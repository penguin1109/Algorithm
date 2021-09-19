# 문자열 조작의 달인
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
S = input().strip()

inf = 10**9 + 7
ans = 0

alph = list(map(chr, range(97, 123)))
change_n = list(map(lambda x: len(alph)-alph.index(x)-1, S))

print(ans % inf)