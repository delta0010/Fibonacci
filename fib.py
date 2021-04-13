def fibo(num):
    if num<=1:return num
    else:return fibo(num-1)+fibo(num-2)

print(" ".join([fibo(i) for i in range(10)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibo(10)
# 34
