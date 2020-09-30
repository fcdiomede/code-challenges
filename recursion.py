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

print_1_through_5_recursively()