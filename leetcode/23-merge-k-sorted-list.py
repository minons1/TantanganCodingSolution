from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res_list = None
    list_map = {}
    if len(lists) == 0:
      return

    for l in lists:
      if l is None:
        continue
      
      while True:
        if list_map.get(l.val, None) is None:
          list_map[l.val] = 1
        else:
          list_map[l.val] += 1

        if l.next is None:
          break
        
        l = l.next
    
    sorted_list_map = sorted(list_map.items(), reverse=True)
    
    for k, v in sorted_list_map:
      while v > 0:
        res_list = ListNode(k, res_list)
        v -= 1
    
    return res_list

sol = Solution()
print(type(sol.mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])) == ListNode)