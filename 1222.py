n = int(input())

for first in range(1, n):
    for second in range(first + 1, n):
        if n % (first + second) == 0:
            print(first, second, sep="", end="")
