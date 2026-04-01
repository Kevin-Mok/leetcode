from typing import Optional
from math import ceil


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        cur = head
        mid = head
        while cur.next:
            length += 1
            cur = cur.next

        for i in range(ceil(length // 2)):
            mid = mid.next
        return mid


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    cur = head
    while cur is not None:
        values.append(cur.val)
        cur = cur.next
    return values


if __name__ == "__main__":
    sol = Solution()
    cases = [
        {
            "head": [1, 2, 3, 4, 5],
            "expected": [3, 4, 5],
        },
        {
            "head": [1, 2, 3, 4, 5, 6],
            "expected": [4, 5, 6],
        },
    ]

    for index, case in enumerate(cases, start=1):
        head = build_linked_list(case["head"])
        print(f"Case {index}")
        print(f"Input: head = {case['head']}")
        try:
            actual_node = sol.middleNode(head)
            actual = linked_list_to_list(actual_node)
            print(f"Actual:   {actual}")
            print(f"Expected: {case['expected']}")
            if actual == case["expected"]:
                print("Match: True")
            else:
                print("Match: False")
                print(f"Diff: actual {actual} != expected {case['expected']}")
        except NotImplementedError as exc:
            print(f"Actual:   raised NotImplementedError: {exc}")
            print(f"Expected: {case['expected']}")
            print("Match: False")
        print()
