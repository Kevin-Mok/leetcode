# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        linked_list1 = ListNode(None)
        linked_list2 = ListNode(None)
        list1_end = linked_list1
        list2_end = linked_list2
        list1_head = linked_list1
        list2_head = linked_list2
        for num in list1:
            list1_end = ListNode(num)
            list1_end = list1_pointer.next
        for num in list2:
            list2_end = ListNode(num)
            list2_end = list2_pointer.next
        
if __name__ == "__main__":
    sol = Solution()
    #  base
    list1 = [1,2,4]
    list2 = [1,3,4]

    #  intertwined
    #  s = "([{}])"

    # wrong
    #  s = "]"

    print(sol.mergeTwoLists(list1, list2))
