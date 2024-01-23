# تابعی که رشته ای را گرفته و در صورت تکراری نبودن حروف  true  برگرداند
def uniq(s):
    for i in range (len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j] :
                return False
    return True
string = input("Enter string : ")
print(uniq(string))   