import time
#نرمال 
# def reverse (a):
#     n = len(a)
#     x = [None]*n
#     for i in range (n):
#         x[n-1-i] = a[i]
#     return x
# my_list = [1,2,3,4,5,6,7,8]
# print(reverse(my_list)) 

# -----------------------
#بهینه تر 

def reverse (a):
    n = len(a)
    for i in range(n // 2):
        a[i] , a[n-1-i] = a[n-1-i] , a[i]
    return a
my_list = [1,2,3,4,5,6,7,8]
print(reverse(my_list)) 