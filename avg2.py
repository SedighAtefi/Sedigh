import time
import random
#نرمال 
start_time = time.time()
def avg(s):
    n = len(s)
    a = [0]*n
    for i in range(n):
        total = 0 
        for j in range(i+1):
            total+=s[j]
        a[i] = total / (j+1)
    return a

num = [random.randint(1,100) for i in range(100)]
print(avg(num))
end_time = time.time()
final_time = round((end_time - start_time),2)
print(final_time)

#بهینه تر

# start_time = time.time()
# def avg (s):
#     n = len(s)
#     a = [0]*n
#     total = 0
#     for i in range(n):
#         total+=s[i]
#         a[i] = total/(i+1)
#     return a
# num = [random.randint(1,100) for i in range(1000000)]
# end_time = time.time()
# final_time = round((end_time - start_time),2)
# print(num)
# print(avg(num))
# print(final_time)