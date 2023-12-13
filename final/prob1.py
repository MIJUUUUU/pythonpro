
string= input("Enter sentence: ")

dic={}

for chr in string:
    if chr in dic:
        dic[chr] += 1 
    else:
        dic[chr]=1

for k,v in dic.items():
     print("{} {}".format(k,v))
