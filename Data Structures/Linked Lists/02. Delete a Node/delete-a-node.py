# sumber link test https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    currentData = head
    currentNode = head
    currentNodee = head

    count = 0
    while currentData is not None :
        currentData = currentData.next
        count += 1
        if count == position + 1 :
            # print(count)
            break

    for i in range(count) :
        currentNode = currentNode.next
        # print(currentNode)

    for i in range(count - 2) :
        currentNodee = currentNodee.next
        # print(currentNodee)
    
    if position == 0 :
        head = head.next
        currentNodee.next = currentNode
    else :
        currentNodee.next = currentNode
            
    return head
    
       