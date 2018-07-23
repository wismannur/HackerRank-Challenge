# sumber link test https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

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
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()