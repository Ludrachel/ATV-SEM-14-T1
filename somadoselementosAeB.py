lis_A = []
lis_B = []

for i in range(20):
    l = int(input())
    lis_A.append(l)
for i in range(20):
    li = int(input())
    lis_B.append(li)

print(lis_A)
print(lis_B)

lis_C = []
for i in range(len(lis_A)):
    lis_C.append(lis_A[i] + lis_B[i])
print(lis_C)
