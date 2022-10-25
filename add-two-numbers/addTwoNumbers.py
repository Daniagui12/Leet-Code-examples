# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize the result
        result = ListNode(0)
        # Initialize the pointer to the result
        result_pointer = result
        # Initialize the carry
        carry = 0
        # Loop through the linked lists
        while l1 or l2:
            # Initialize the sum
            sum = 0
            # If l1 is not None
            if l1:
                # Add the value of l1 to the sum
                sum += l1.val
                # Move l1 to the next node
                l1 = l1.next
            # If l2 is not None
            if l2:
                # Add the value of l2 to the sum
                sum += l2.val
                # Move l2 to the next node
                l2 = l2.next
            # Add the carry to the sum
            sum += carry
            # If the sum is greater than 9
            if sum > 9:
                # Set the carry to 1
                carry = 1
                # Set the sum to the remainder of the sum divided by 10
                sum = sum % 10
            # Else
            else:
                # Set the carry to 0
                carry = 0
            # Set the result pointer to the sum
            result_pointer.val = sum
            # If l1 or l2 is not None
            if l1 or l2:
                # Set the next node of the result pointer to a new node
                result_pointer.next = ListNode(0)
                # Move the result pointer to the next node
                result_pointer = result_pointer.next
        # If the carry is 1
        if carry == 1:
            # Set the next node of the result pointer to a new node
            result_pointer.next = ListNode(1)
        # Return the result
        return result