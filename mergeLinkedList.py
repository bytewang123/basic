class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newL, node = None, None

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                if node == None:
                    node = ListNode(l1.val)
                    newL = node
                else:
                    node.next = ListNode(l1.val)
                    node = node.next

                l1 = l1.next

            else:
                if node == None:
                    node = ListNode(l2.val)
                    newL = node
                else:
                    node.next = ListNode(l2.val)
                    node = node.next

                l2 = l2.next
                        
        if l1 == None:
            while l2 != None:
                if node == None:
                    node = ListNode(l2.val)
                    newL = node
                else:
                    node.next = ListNode(l2.val)
                    node = node.next
                l2 = l2.next

        if l2 == None:
            while l1 != None:
                if node == None:
                    node = ListNode(l1.val)
                    newL = node
                else:
                    node.next = ListNode(l1.val)
                    node = node.next
                l1 = l1.next
            

        return newL               

        


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l4.next = l5
l5.next = l6


ret = mergeTwoLists(l1, l4)
while ret != None:
    print ret.val
    ret = ret.next
