from collections import deque
# import sys
# input = sys.stdin.readline

f = open('BoJ/test.txt')

N = int(f.readline())
region = [list(map(int,f.readline().split())) for _ in range(N)]

 