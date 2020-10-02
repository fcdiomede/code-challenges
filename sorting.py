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

# print(sort_ab(a,b))

#missing number
def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    midpoint = len(nums) // 2
    
    lo, equal, high = [], [], []

    for num in nums:
        if num < nums[midpoint]:
            lo.append(num)
        elif num == nums[midpoint]:
            equal.append(num)
        else:
            high.append(num)
    
    return quick_sort(lo) + equal + quick_sort(high)


def missing_number(nums, max):
    sorted_nums = quick_sort(nums)
    
    for i in range(max):
        if sorted_nums[i] != i+1:
            return i+1

# print(missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10))

def mathy_missing_number(nums, max):
    expected = sum(range(max+1))

    return expected - sum(nums)

# print(mathy_missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10))

#coins
#You have an endless supply of dimes and pennies. How many different amounts of 
#total change can you make using exactly num_coins number coins?
# For example, when num_coins = 3, you can create 4 different kinds of change:

# 3 cents from penny + penny + penny

# 12 cents dime + penny + penny

# 21 cents from dime + dime + penny

# 30 cents from dime + dime + dime

# So, you should have a function that returns the set {3, 12, 21, 30} when num_coins is 3.

#first, add together number of coins if it was all pennies
#then, would switch each out for a dime (add 9 to my sum)
#do this a number of times equal to how many coins I had. 

def coins(num_coins):
    #start my change value in number of pennies
    current_change = num_coins

    #initalize a set with my current change val
    change = {current_change}
    num_dimes = 0

    while num_dimes < num_coins:
        current_change += 9
        change.add(current_change)
        num_dimes += 1
    
    return change

# print(coins(1))
# print(coins(3))

#implement insertion sort
def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""
    for index in range(1,len(alist)):
        #item to be inserted in correct position
        key = alist[index]
        #look to the right of item I want to insert
        sublist_index = index - 1

        #while I haven't reached the end of the sublist or key item is smaller
        while sublist_index >= 0 and key < alist[sublist_index]:
            #want to shift larger item over
            alist[sublist_index + 1] = alist[sublist_index]
            #decrement by 1 so I look at next item over to the left on next
            #iteration
            sublist_index -= 1
        #once I have stopped looping because I am either at beginging of list
        #or because I found an item that is smaller than the key, insert the key
        #to the right
        alist[sublist_index+1] = key
    
    return alist

#merge sort

#base case - list of one
#merge already sorted lists together

def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    midpoint = len(lst) // 2
    lst1 = merge_sort(lst[:midpoint])
    lst2 = merge_sort(lst[midpoint:])

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):
    print("list 1: ", lst1)
    print("list 2: ", lst2)

    result = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(lst1) and index_2 < len(lst2):
        if lst1[index_1] <= lst2[index_2]:
            result.append(lst1[index_1])
            index_1 += 1
        else:
            result.append(lst2[index_2])
            index_2 += 1
    
    if index_1 == len(lst1):
        result.extend(lst2[index_2:])
    else:
        result.extend(lst1[index_1:])
    
    return result




