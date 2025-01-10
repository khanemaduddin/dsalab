class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def reverse_linked_list(head: Node) -> Node:
    if not head:
        return None  # if the list is empty, return None

    prev, current = None, head
    while current:
        next_node = current.next  # store the next node
        current.next = prev       # reverse the link
        prev = current            # move prev to current
        current = next_node       # move to the next node

    return prev  # prev will be the new head after the loop ends

# Helper function to print a linked list
def display_linked_list(head: Node):
    current = head
    while current:
        print(current.value, end="->" if current.next else "\n")
        current = current.next

# Example usage:
# Creating linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
display_linked_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed list:")
display_linked_list(reversed_head)

