"""
About:
    2022/01/20 - Python LinkedList - V.0.2.0 - A.Ragalzi
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
"""

from __future__ import annotations


from typing import Generator


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
        return 'Node()'

    def __str__(self):
        return f'data: {self.data}, next_node: {self.next_node}'

    @property
    def data(self) -> any:
        return self.__data

    @property
    def next_node(self) -> Node | None:
        return self.__next_node

    @data.setter
    def data(self, data: any) -> None:
        self.__data = data

    @next_node.setter
    def next_node(self, next_node: Node = None) -> None:
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
        return 'LinkedList()'

    def __str__(self):
        str_linked_list = ''
        current = self.head
        while current is not None:
            str_linked_list += f'{current.data} -> '
            current = current.next_node
        return str_linked_list[:-4]

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
        return self.__head

    @head.setter
    def head(self, head: Node | None) -> None:
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
        return self.__lenght

    @lenght.setter
    def lenght(self, lenght: int) -> None:
        self.__lenght = lenght


if __name__ == '__main__':
    llist1 = LinkedList(0, 1, 2, 3)
    print(llist1)
    llist1.insert(2, 99)
    print(llist1)
    llist1.insert(0, 100)
    print(llist1)
