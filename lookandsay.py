def next_num(s):
    result=[]
    i=0
    while i<len(s):
        count =1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            count+=1
        result.append(str(count) + s[i])
        i+=1
    return "".join(result)
s= "1121"
#print(next_num(s))


def anagram(s1, s2):
    ht =dict()

    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i in ht:
            ht[i]+=1
        else:
            ht[i]=1
        
    for i in s2:
        if i in ht:
            ht[i]-=1
        else:
            ht[i]=1
        
    for i in ht:
        if ht[i]!=0:
            return False
    return True
s3="abcd"
s4="dcad"
print(anagram(s3, s4))