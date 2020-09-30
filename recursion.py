#challenge 1
#Write a recursive function that takes in a list and prints each element in that list.

def print_recursively(item_list):
    #base case list of 1 item

   if len(item_list) > 0:
       print(item_list[0])
       print_recursively(item_list[1:])

print_recursively(["apple", "berry", "cherry"])
print_recursively(["apple"])
print_recursively([])