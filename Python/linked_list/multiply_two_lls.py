# Python program to Multiply two linkedlists

# Linked List Node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class singly_linked_list():
    def __init__(self):
        self.head = None

    def add(self, node):
        '''
        Add a node the linked list.
        '''
        if not self.head:
            # If no nodes exist, assign the new node to the head node.
            self.head = node
        else:
            # Link the old stuff to the new node
            node.next = self.head
            # Move the head node to point to the new node
            self.head = node

    def __repr__(self):
        '''
        Returns a string object containing a representation
        of the linked list.
        '''
        next = self.head
        str_repr = ""
        while(next):
            str_repr += str(next.data)
            if next.next: str_repr += "->"
            next = next.next
        return str_repr

def multiply_linked_lists(list1, list2):
    '''
    Generates the numberic representation of 2 linked lists
    and returns their product.
    '''
    first_number = 0
    second_number = 0

# Generate the first number
    next = list1.head
    while next:
        first_number = first_number*10+next.data
        next = next.next

# Generate the second number
    next = list2.head
    while next:
        second_number = second_number*10+next.data
        next = next.next

# Return the product
    return first_number*second_number



# Instantiate 2 linked lists
l_list1 = singly_linked_list()
l_list2 = singly_linked_list()

# Create first list
l_list1.add(Node(6))
l_list1.add(Node(4))
l_list1.add(Node(9))

# Create second list
l_list2.add(Node(4))
l_list2.add(Node(8))

print("First list is: ", l_list1)
print("Second list is: ", l_list2)

print("Results is: ", multiply_linked_lists(l_list1, l_list2))

