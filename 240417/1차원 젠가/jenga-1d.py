n = int(input())
blocks = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split()) # 위에서 s1번째부터 e1번째까지 블럭을 제거
s2, e2 = map(int, input().split()) # 동일

blocks = blocks[:s1-1] + blocks[e1:]
blocks = blocks[:s2-1] + blocks[e2:]

print(len(blocks))
for block in blocks:
    print(block)