def array_advance(a):
    last_index= len(a)-1
    furthes_reached=0
    i=0
    while i<=furthes_reached and furthes_reached<last_index:
        furthes_reached=max(furthes_reached, a[i]+i)
        i+=1

    return furthes_reached>=last_index

b=[3,2,0,0,1]
print(array_advance(b))