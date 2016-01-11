def recursiveFibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibo(n - 1) + recursiveFibo(n - 2)


def itterFibo(n):
    fib = 0
    a = 1
    t =0
    for i in range(n):
        t = fib + a
        a = fib
        fib = t
    return fib


from time import time
n = [10, 100, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]
recursiveTime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
itterTime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for j in range(11):
    print(j)
    print("n")
    timeStart = time()
    print(itterFibo(n[j]))
    itterTime[j] = time() - timeStart
    print(" done\n")

n2 = [5, 10, 15, 20, 25, 30, 33, 36, 39, 40, 41]
for j in range(11):
    print(j)
    print("n")
    timeStart = time()
    print(recursiveFibo(n2[j]))
    recursiveTime[j] = time() - timeStart
    print(" done\n")

f = open("timeData.txt", "w")
f.write("n, " + str(n2))
f.write("\n ")
f.write("RecursiveTime, " + str(recursiveTime))
f.write("\n")
f.write("n, " + str(n))
f.write("\n")
f.write("ItterativeTime, " + str(itterTime))
f.write("\n")
f.close()
print("done")