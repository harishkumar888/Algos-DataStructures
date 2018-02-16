# LinkedList traversal

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, node):
        if not self.head or not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def size(self):
        return self.length

    def contains(self, node):
        next = self.head
        while(next):
            if next.data == node.data:
                return True
            else:
                next = next.next
        return False

    def get_linked_list(self):
        llist = []
        next = self.head
        while(next):
            llist.append(next.data)
            next = next.next
        return llist

    def __repr__(self):
        return str(self.get_linked_list())

    def rotate(self, k):
        for i in range(k):
            cur_head_node = self.head
            cur_tail_node = self.tail
            self.head = cur_head_node.next
            cur_tail_node.next = cur_head_node
            new_tail_node = cur_tail_node.next
            new_tail_node.next = None
            self.tail = cur_tail_node.next

    def reverse(self):
        cur_node = self.head
        prev_node = None
        next_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def DeleteNode(self, head, node):
      if not self.head: return
      if self.head.value == node:
        self.head =self.head.next
      prev = temp_node = self.head
      while temp_node:
        if temp_node.value == node:
          prev.next = temp_node.next
          temp_node.next = None
          break
        else:
          prev = temp_node
          temp_node = temp_node.next

    def get_dummy_ll(self):
        for i in range(1,9):
            self.add(Node(i))

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head is None: return
    if head.next is None: return
    current = head
    count = 1
    while current.next:
        current = current.next
        count += 1

    current.next = head
    for i in range(count-k-1):
        head = head.next

    prev = head
    head = head.next
    prev.next = None
    return head

def multiply_linked_lists(list1, list2):
    '''
    Input : 9->4->6 = 946
            8->4    =84
    Output : 79464 (946*84)

    Input : 3->2->1 = 321
            1->2    = 12
    Output : 3852 (321*12)
    '''
    first_number = 0
    second_number = 0
    next = list1.head
    while next:
        first_number = first_number*10+next.data
        next = next.next
    next = list2.head
    while next:
        second_number = second_number*10+next.data
        next = next.next
    return first_number*second_number




ll1 = SinglyLinkedList()
ll2 = SinglyLinkedList()

# for i in range(1, 4, 1):
#     ll1.add(Node(i))
#     ll2.add(Node(i+2))

# print(ll1)
# print(ll2)
# print(multiply_linked_lists(ll1, ll2))
# # ll1.reverse()
# # print(ll1)

# # 1->2->3->4
# # 
ll1.get_dummy_ll()
print(ll1)
ll1.rotate(2)
print(ll1)
