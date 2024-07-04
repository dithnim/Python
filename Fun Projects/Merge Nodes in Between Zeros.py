# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

# Return the head of the modified linked list.

 

# Example 1:


# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.
# Example 2:


# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.
 

# Constraints:

# The number of nodes in the list is in the range [3, 2 * 105].
# 0 <= Node.val <= 1000
# There are no two consecutive nodes with Node.val == 0.
# The beginning and end of the linked list have Node.val == 0.

#!Using loops
# def mergeNodesUsingFor(head):
#     out = []
#     temp = 0
#     for i in head:
#         if head[i] == 0 and i != 0:
#             out.append(temp)
#             temp = 0
#         temp += head[i]

#     return out


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    # Initialize pointers
    current = head.next  # Skip the first zero
    new_head = ListNode()  # Dummy node for the new linked list
    new_tail = new_head
    
    sum_val = 0  # To accumulate the sum between zeros
    
    while current:
        if current.val == 0:
            # When we reach a zero, it means we have completed one segment
            new_tail.next = ListNode(sum_val)
            new_tail = new_tail.next
            sum_val = 0  # Reset the sum for the next segment
        else:
            sum_val += current.val
        current = current.next
    
    return new_head.next  # Return the new list, skipping the dummy node

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)

# Example usage
head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
merged_list = mergeNodes(head)
print_linked_list(merged_list)  # Output: [4, 11]

head2 = create_linked_list([0, 1, 0, 3, 0, 2, 2, 0])
merged_list2 = mergeNodes(head2)
print_linked_list(merged_list2)  # Output: [1, 3, 4]


