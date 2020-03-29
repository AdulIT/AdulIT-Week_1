H = int(input())
A = int(input())
B = int(input())
up = 0
count = 0
up = up + A
count = count + 1
while up < H:
    up = up - B + A
    count = count + 1
print(count)
