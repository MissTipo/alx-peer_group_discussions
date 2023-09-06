'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again
    by continuously following the next pointer. Internally, pos is used to denote the index of the
    node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

Input: head = [3,2,0,-4], pos = -1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

def hasCycle(self, head: Optional[ListNode]) -> bool:
    
    if lenght of list is less or equal to 1:
        return False

    if pos is an index in the list other than the last(tail) index:
        return True

    if pos is >= index of tail:
        return False


    node_list = []
    move from head:
        append each node value to node_list 
        check if current node value is already in node_list:

        if current->next:
            # if current->next in node_list:
            
                if current->next is not last element:
                    return True
            else:
                add current->next to the set



            
            if current->next is null:
                return False

            if false:
                continue
            if True:
                if the alement is not the last element in the list:
                    return True

        
'''


def hasCycle(h):

    node_set = set()

    # current = h

    while h:
        if h.next:
            if (h.val in node_set) and (h.next != h.val):
                return True
            else:
                node_set.add(h.val)

            h = h.next
        else:
            return False
