n, t = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

for _ in range(t):
    first_tmp = first.pop()
    second_tmp = second.pop()
    third_tmp = third.pop()

    first = [third_tmp] + first
    second = [first_tmp] + second
    third = [second_tmp] + third


print(*first)
print(*second)
print(*third)