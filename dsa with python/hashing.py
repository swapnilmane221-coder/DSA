num=[2,5,6,8,10,12,14,16,18,20,5,8,4,2,6,9,11,13,15,17,19]
count={}
for i in num:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)