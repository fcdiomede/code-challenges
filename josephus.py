class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)

def create_circular_linked_list(number_nodes):
    #make the first node
    first = prev = Node(1)

    for num in range(2, number_nodes+1):
        node = Node(num)
        node.prev = prev
        node.prev.next = node
        prev = node

    #modify first and previous to match
    node.next = first
    first.prev = node

    return first

def print_nodes(head):
    print(head.data)
    current = head.next
    while current is not head:
        print(current.data)
        current = current.next

#testing
# survivor_list = create_circular_linked_list(10)
# print_nodes(survivor_list)

def find_survivor(num_people, kill_every):

    current = create_circular_linked_list(num_people)
    count = 1
    while current.next is not current:
        if count == kill_every:
            current.prev.next = current.next
            current.next.prev = current.prev
            count = 1
        else:
            count += 1
        current = current.next
    
    return current.data


print(find_survivor(10, 3))

