# x = ['kunal', 'adhav']

# for i in x:
#     x.append(i.upper())
# print(x)


# n = 124894
# l = len(str(n))
# sum = 0
# for i in range(l):
#     sum = i + n % 10
#     break
# print(sum)

x = [11, 12, 13, 8, 10]
count = 0
for i in x:
    if i >= 10:
        count += 1
    else:
        count += 0
print(count)


for _ in range(T):
    X, Y, Z = map(int, input().split())
    k = 0
    while (X * Y) > Z:
        X += X
        k += 1
    print(k)
