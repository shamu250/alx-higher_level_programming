#!/usr/bin/python3

class SinglyLinkedList:
    ''' class SinglyLinkedList '''

    def __init__(self):
        self.__head = None

    def __str__(self):
        ''' string representation of Singly Linked List '''
        tmp = self.__head
        while tmp is not None:
            print(type(tmp), end='')
            print(tmp)
            tmp = tmp.next_node

    def sorted_insert(self, value):
        ''' insert new node at proper position
        (sorted) ascending order '''
        self.__head.append(Node(value))

    def insert_at_end(self, value):
        ''' insert at end of SLL '''
        if self.__head is None:
            self.__head = Node(value)
            print("first insert {}".format(self.__head))
        else:
            print("InAtEnd=======")
            tmp = self.__head
            print("----ID{}".format(id(tmp)))
            while(tmp.next_node is not None):
                tmp = tmp.next_node
                print("+++++ID{}".format(id(tmp)))
            print("what is value --> {}".format(str(value)))
            # tmp.next_node = Node(value)
            tmp = Node(value)
            print("jus before end - {}".format(tmp))
            # print("NODEatEND-> {}".format(tmp.next_node))

class Node:
    '''Hello from class Node'''

    def __init__(self, data, next_node=None):
        '''init instance of Node class'''
        self.data = data
        self.next_node = next_node

    def __str__(self):
        '''print a node instance '''
        print(self.__data)

    @property
    def data(self):
        ''' hello! '''
        return self.__data
        
    @data.setter
    def data(self, value):
        '''data setter'''
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''hello! from next_node getter '''
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        '''next node setter'''
        if not(next_node is None or type(next_node) == Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
