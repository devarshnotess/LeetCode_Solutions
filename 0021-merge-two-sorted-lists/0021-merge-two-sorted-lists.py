# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        # intialize the Dummy node named si which can help build the merged linked list
        si = ListNode()
        present = si

        # Now we compare the two nodes of the lists and attach the smaller one to the merged list
        while list1 and list2:
            if list1.val > list2.val:
                present.next = list2
                list2 = list2.next  # Move to the Next node in list2
            else:
                present.next = list1
                list1 = list1.next  # Move to the next node in list1
            
            present = present.next  # Continue the Tail of the merged list
        
        # At the end one list remains attach it directly because its remaining nodes are already sorted

        if list1:
            present.next = list1
        else:
            present.next = list2

        # Return the Head of the actual merged list
        return si.next

