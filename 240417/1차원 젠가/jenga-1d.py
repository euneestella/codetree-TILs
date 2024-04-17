n = int(input())
blocks = [int(input()) for _ in range(n)]
end_of_array = n


def cut_array(start_idx, end_idx):
    global end_of_array, blocks

    temp_arr = []

    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(blocks[i])
    
    end_of_array = len(temp_arr)
    for i in range(end_of_array):
        blocks[i] = temp_arr[i]
    

for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s - 1, e - 1)

print(end_of_array)
for i in range(end_of_array):
    print(blocks[i])