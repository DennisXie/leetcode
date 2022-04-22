class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """此题可以的list实际上是个中序遍历，采用类似中序遍历的方式可以还原BST，时间复杂度为O(n)"""

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.build(head, None)

    def build(self, head: ListNode, tail: ListNode) -> TreeNode:
        mid = self.findMiddle(head, tail)

        if mid is None:
            return None

        left = self.build(head, mid)
        right = self.build(mid.next, tail)
        node = TreeNode(mid.val, left, right)
        return node

    def findMiddle(self, head: ListNode, tail: ListNode, left: bool = True) -> ListNode:
        slow = head
        fast = head
        count = 1
        while fast != tail and fast is not None:
            fast = fast.next
            count += 1
            if count & 1 == 0 and count != 2:
                slow = slow.next

        count -= 1
        if count == 0:
            return None
        elif count & 1 == 0:
            return slow if left else slow.next
        else:
            return slow
