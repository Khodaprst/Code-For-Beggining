def NumMax(a, b, c):
    maxNum = a if a > b else b
    maxNum = c if c > maxNum else maxNum
    return maxNum
x = int(input())
y = int(input())
z = int(input())
m = NumMax(x, y, z)
print(m)