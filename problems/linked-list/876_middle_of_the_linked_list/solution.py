from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        current = head

        while current:
            nodes.append(current)
            current = current.next

        return nodes[len(nodes) // 2]