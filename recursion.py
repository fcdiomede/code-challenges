#challenge 1
#Write a recursive function that takes in a list and prints each element in that list.

def print_recursively(item_list):
    #base case list of 1 item

   if len(item_list) > 0:
       print(item_list[0])
       print_recursively(item_list[1:])

# print_recursively(["apple", "berry", "cherry"])
# print_recursively(["apple"])
# print_recursively([])

#challenge 2
#Write a recursive function that prints the numbers 1 through 5.

def print_1_through_5_recursively(num=1):
    #base case is number at 5
    #with a loop:
    # num = 1
    # while num < 5:
    #     print(num)
    #     num += 1
    
    if num > 5:
        return
    
    print(num)
    print_1_through_5_recursively(num+1)

# print_1_through_5_recursively()

#challenge 3
#Write a recursive function that takes a list of numbers and returns the largest number in the list.

def largest_num(num_list, max_n=None):
    print(max_n)

    if len(num_list) > 0 and max_n is None:
        max_n = num_list[0]

    if len(num_list) <= 1:
        return max_n
    
    n = num_list.pop()
    if n > max_n:
        max_n = n

    return largest_num(num_list, max_n)


print(largest_num([1,2,3,4,5]))
print(largest_num([9,5,7,1]))
print(largest_num([]))