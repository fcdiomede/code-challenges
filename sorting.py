#sort sorted lists
def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    #keep track of where I am in list a and list b
    #compare and add lowest num between a and b
    #move the tracker up for what ever I just added
    #do this until I've reached the end of both lists

    index_a = 0
    index_b = 0
    result=[]
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1
        
    if index_a == len(a):
        #must have already appended everything in list a, so add whatever is
        #left in list b
        result.extend(b[index_b:])
    else:
        result.extend(a[index_a:])
    
    return result

a = [1,3,5]
b = [2,6,9]

#i-a: 3
#i-b: 1
#[1,2,3,5,6,9]

print(sort_ab(a,b))