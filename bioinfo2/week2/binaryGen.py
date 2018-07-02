import math

n = 3

ceiling = 0

for x in range(n):
    ceiling += int(math.pow(2,x))

for i in xrange(ceiling+1):
    b = bin(i)[2:]
    l = len(b)
    b = str(0) * (n - l) + b  
    print b
