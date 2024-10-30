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
        if list1 == None:
            if list2 == None:
                return None
            return list2
        elif list2 == None:
            return list1

        sorted_head = None
        list1_end = list1
        list2_end = list2
        if list1_end.val <= list2_end.val:
            sorted_head = list1
            list1_end = list1_end.next
        else:
            sorted_head = list2
            list1_end = list2_end.next

        sorted_end = sorted_head
        while (list1_end != None) and \
            (list2_end != None):
                if list1_end.val <= list2_end.val:
                    sorted_end.next = list1_end
                    list1_end = list1_end.next
                else:
                    sorted_end.next = list2_end
                    list2_end = list2_end.next
                sorted_end = sorted_end.next

        if list1_end == None:
            sorted_end.next = list2_end
        elif list2_end == None:
            sorted_end.next = list1_end
        # if list1_end.val > list2_end.val:
            # sorted_end.next = list1_end
        # else:
             # sorted_end.next = list2_end

        return sorted_head
        
if __name__ == "__main__":
    sol = Solution()
    #  base
    # 

    #  1
    # list1 = [1,2,4]
    # list1_2 = ListNode(4)
    # list1_1 = ListNode(2, list1_2)
    # list1 = ListNode(1, list1_1)
    # # list2 = [1,3,4]
    # list2_2 = ListNode(4)
    # list2_1 = ListNode(3, list2_2)
    # list2 = ListNode(1, list2_1)
    # sorted = [1,1,2]
    # sorted_head = [1]
    # list1_end = [4]
    # list2_end = [3]
    # sorted_end = [4]
    #  expected = [1,1,2,3,4,4]

    # list1_1 = ListNode(2)
    # list1 = ListNode(1, list1_1)
    # list2_1 = ListNode(4)
    # list2 = ListNode(3, list2_1)

    list1 = ListNode(2)
    list2 = ListNode(1)

    #  6
    #  list1 = [3]
    #  list2 = [1,2]
    #  sorted = [1]
    #  sorted_head = [1]
    #  list1_end = [2]
    #  list2_end = [3]
    #  sorted_end = [1]
    #  expected = [1,2,3]

    #  4
    #  list1 = [1,2]
    #  list2 = [3]
    #  sorted_head = [1]
    #  sorted = [1,2]
    #  list1_end = []
    #  list2_end = [3]
    #  sorted_end = [1]
    #  expected = [1,2,3]

    #  5
    #  list1 = [1,2]
    #  list2 = []
    #  sorted = [1]
    #  sorted_head = [1]
    #  list1_end = [2]
    #  list2_end = [3]
    #  sorted_end = [1]
    #  expected = [1,2]

    #  3
    #  list1 = []
    #  list2 = [0]
    #  expected = [0]

    #  2
    # list1 = []
    # list2 = []
    # expected = []

    # wrong
    #  s = "]"

    print(sol.mergeTwoLists(list1, list2))
