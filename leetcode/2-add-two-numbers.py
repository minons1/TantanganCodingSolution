
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur_l1, cur_l2 = l1, l2
        res = ''
        while cur_l1 is not None or cur_l2 is not None or carry != 0:
            l1_val = cur_l1.val if cur_l1 is not None else 0
            l2_val = cur_l2.val if cur_l2 is not None else 0
            print(l1_val, l2_val)

            sum = l1_val + l2_val + carry

            val, carry = sum % 10, sum // 10
            res = res + str(val)

            cur_l1 = cur_l1.next if cur_l1 is not None else None
            cur_l2 = cur_l2.next if cur_l2 is not None else None
        
        res_ll = None
        for digit in reversed(res):
            res_ll = ListNode(digit, res_ll)
        
        return res_ll

sol = Solution()
# ll = sol.addTwoNumbers(
#     ListNode(2,
#         ListNode(4,
#             ListNode(3, None))),
#     ListNode(5,
#         ListNode(6,
#             ListNode(4, None))))

# ll = sol.addTwoNumbers(ListNode(0, None), ListNode(0, None))

ll = sol.addTwoNumbers(
    ListNode(9,
        ListNode(9,
            ListNode(9,
                ListNode(9, None)))),
    ListNode(9, ListNode(9, None))
)

while ll is not None:
    print(ll.val, end='')
    ll = ll.next
