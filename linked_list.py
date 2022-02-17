"""
About:
    2022/02/17 - Python LinkedList - V.22.2.1 - A.Ragalzi
Description:
   Module that implement singly linked list in Python
Function:
    None
Class:
    Node Method:
        @property
        data(self) -> any
        @property
        next_node(self) -> Node | None
        @data.setter
        data(self, data: any) -> None
        @next_node.setter
        next_node(self, next_node: Node = None) -> None
    LinkedList Method:
        clear(self) -> None
        delete_by_index(self, pos: int) -> None
        delete_by_node(self, target_node: Node) -> None
        delete_by_value(self, data: any) -> None
        delete_head(self) -> None
        delete_tail(self) -> None
        @property
        head(self) -> Node | None
        @head.setter
        head(self, head: Node | None) -> None
        insert(self, pos: int, data: any) -> None
        insert_head(self, data: any) -> None
        insert_tail(self, data: any) -> None
        @property
        lenght(self) -> int
        @lenght.setter
        lenght(self, lenght: int) -> None
Function:
    insert_linked_list(llist1: LinkedList, llist2: LinkedList) -> None
"""

from __future__ import annotations

from typing import Generator


def insert_linked_list(llist1: LinkedList, llist2: LinkedList) -> None:
    """Insert llist2 in llist1

    Args:
        llist1 (LinkedList): linked list to extend
        llist2 (LinkedList): linked list to insert

    Example:
        llist1 = 3 -> 4 -> 1 -> 7
        llist2 = 4 -> 9 -> 0
        insert_linked_list(llist1, llist2)
        print(llist1)
        ~ 3 -> 4 -> 9 -> 0-> 1 -> 7
    """
    if len(llist1) == 0 or len(llist1) == 0:
        raise ValueError('linked list is empty')
    current = llist1.head
    found = False
    i = 0
    while current is not None:
        if current.data == llist2.head.data:
            for j, value in enumerate(llist2):
                if j > 0:
                    llist1.insert(i, value)
                i += 1
            found = True
            break
        else:
            current = current.next_node
            i += 1
    if not found:
        raise ValueError('value not found in linked list')


class Node:
    """Class that represents a node of a linked list"""

    def __init__(self, data: any = None):
        self.__data = data
        self.__next_node = None

    def __eq__(self, target_node: Node) -> bool:
        if isinstance(target_node, Node):
            if self.data == target_node.data:
                return True
        return False

    def __repr__(self):
        return f'Node({self.data})'

    def __str__(self):
        return f'data: {self.data}, next_node: {self.next_node}'

    @property
    def data(self) -> any:
        """Get data"""
        return self.__data

    @property
    def next_node(self) -> Node | None:
        """Get next node"""
        return self.__next_node

    @data.setter
    def data(self, data: any) -> None:
        """Set data"""
        self.__data = data

    @next_node.setter
    def next_node(self, next_node: Node = None) -> None:
        """Set next node"""
        self.__next_node = next_node


class LinkedList:
    """Class that represents a singly linked list"""
    __lenght = 0

    def __init__(self, *values: any):
        if len(values) == 0:
            self.head = None
        else:
            current = Node(values[0])
            self.head = current
            self.lenght = self.lenght + 1
            for data in values[1:]:
                current.next_node = Node(data)
                current = current.next_node
                self.lenght = self.lenght + 1

    def __iter__(self) -> Generator[any, None, None]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next_node

    def __eq__(self, target_llist: LinkedList) -> bool:
        res = False
        if isinstance(target_llist, LinkedList):
            if len(self) == len(target_llist):
                res = True
                for node1, node2 in zip(self, target_llist):
                    if node1 != node2:
                        res = False
                        break
        return res

    def __len__(self) -> int:
        return self.__lenght

    def __repr__(self):
        repr_linked_list = ''
        current = self.head
        while current is not None:
            repr_linked_list += f'{current.data}, '
            current = current.next_node
        return f'LinkedList({repr_linked_list[:-2]})'

    def __str__(self):
        str_linked_list = ''
        current = self.head
        while current is not None:
            str_linked_list += f'{current.data}\n'
            current = current.next_node
        return str_linked_list[:-1]

    def clear(self) -> None:
        """Empty the linked list"""
        self.head = None
        self.lenght = 0

    def delete_by_index(self, pos: int) -> None:
        """Delete a node in a specific position"""
        if len(self) == 0:
            raise ValueError('linked list is empty')
        if pos < 0 or pos > len(self):
            raise ValueError('pos doesn\'t exists')
        count = 0
        current = self.head
        previous = self.head
        while current is not None or count < pos:
            if count == pos:
                if pos == 0:
                    self.delete_head()
                else:
                    previous.next_node = current.next_node
                    self.lenght = self.lenght - 1
                break
            else:
                previous = current
                current = current.next_node
            count += 1

    def delete_by_node(self, target_node: Node) -> None:
        """Delete a node by node"""
        if not isinstance(target_node, Node):
            raise TypeError('node must be a Node')
        if len(self) == 0:
            raise ValueError('linked list is empty')
        current = self.head
        previous = None
        found = False
        while not found:
            if current == target_node:
                found = True
            elif current is None:
                raise ValueError('node not found in linked list')
            else:
                previous = current
                current = current.next_node
        if previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node
        self.lenght = self.lenght - 1

    def delete_by_value(self, data: any) -> None:
        """Delete a node by data"""
        if len(self) == 0:
            raise ValueError('linked list is empty')
        current = self.head
        previous = self.head
        found = False
        if current.data == data:
            found = True
            self.delete_head()
        else:
            while current is not None:
                if current.data == data:
                    previous.next_node = current.next_node
                    self.lenght = self.lenght - 1
                    found = True
                    break
                else:
                    previous = current
                    current = current.next_node
        if not found:
            raise ValueError('value not found in linked list')

    def delete_head(self) -> None:
        """Delete head"""
        if len(self) == 0:
            raise ValueError('linked list is empty')
        else:
            self.head = self.head.next_node
            self.lenght = self.lenght - 1

    def delete_tail(self) -> None:
        """Delete tail"""
        if len(self) == 0:
            raise ValueError('linked list is empty')
        else:
            current = self.head
            previous = self.head
            while current.next_node is not None:
                previous = current
                current = current.next_node
            previous.next_node = None
            self.lenght = self.lenght - 1

    @property
    def head(self) -> Node | None:
        """Get head"""
        return self.__head

    @head.setter
    def head(self, head: Node | None) -> None:
        """Set head"""
        self.__head = head

    def insert(self, pos: int, data: any) -> None:
        """Insert a new node in a specific pos."""
        if pos < -1 or pos > len(self):
            raise ValueError('pos out of linked list range')
        elif pos == 0:
            self.insert_head(data)
        else:
            new_node = Node()
            new_node.data = data
            current = self.head
            count = 0
            while count < pos-1:
                current = current.next_node
                count += 1
            new_node.next_node = current.next_node
            current.next_node = new_node
            self.lenght = self.lenght + 1

    def insert_head(self, data: any) -> None:
        """Insert a new head"""
        new_node = Node()
        new_node.data = data
        if len(self) == 0:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.lenght = self.lenght + 1

    def insert_tail(self, data: any) -> None:
        """Insert a new tail"""
        if len(self) == 0:
            self.insert_head(data)
        else:
            new_node = Node()
            new_node.data = data
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node
            self.lenght = self.lenght + 1

    @property
    def lenght(self) -> int:
        """Get lenght"""
        return self.__lenght

    @lenght.setter
    def lenght(self, lenght: int) -> None:
        """Set lenght"""
        self.__lenght = lenght


if __name__ == '__main__':
    pass
