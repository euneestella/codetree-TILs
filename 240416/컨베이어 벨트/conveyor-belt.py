n, t = map(int, input().split())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    top_tmp = top.pop()
    bottom_tmp = bottom.pop()
    top = [bottom_tmp] + top
    bottom = [top_tmp] + bottom

print(*top)
print(*bottom)