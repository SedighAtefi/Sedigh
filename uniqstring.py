import time
start_time = time.time()
# def disjoint (A,B,C):
#     for a in A:
#         for b in B : 
#             for c in C :
#                 if a == b == c :
#                     return False
#     return True

# a = input("Enter first string : ")
# b = input("Enter secend string : ")
# c = input("Enter theird string : ")

# print(disjoint(a,b,c))
end_time = time.time()
final_time = round((end_time - start_time),2)
print(final_time)

#--------------------------------

a = input("Enter first string : ")
b = input("Enter secend string : ")
c = input("Enter theird string : ")

start_time = time.time()
def disjoint (A,B,C):
    for a in A:
        for b in B : 
            if a == b :
                for c in C :
                    a == C
                    return False
    return True
end_time = time.time()
final_time = round((end_time - start_time),2)
print(disjoint(a,b,c))
print(final_time)