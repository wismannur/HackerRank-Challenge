# sumber link test https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    print(head.data)
    while head is not None :
        head = head.next
        print(head.data)