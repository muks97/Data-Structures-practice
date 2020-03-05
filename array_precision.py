A= [9,9,9]

def array_precise(a):
    a[-1]+=1
    for i in reversed(range(1, len(a))):
        if a[i]!=10:
            break
        else:
            a[i]= 0
        
            a[i-1]+=1
            
    if a[0]==10:
        a[0]=1
        a.append(0)
    return a

print(array_precise(A))