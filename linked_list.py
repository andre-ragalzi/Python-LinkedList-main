"""
About:
    2022/01/19 - Python LinkedList - V.0.1.0 - Gefit UTW - A.Ragalzi
Description:
   Module that implement singly linked list in Python
Class:
    LinkedList
    Method:
        clear(self) -> None
        delete_by_data(self, data: any) -> None
        delete_by_index(self, pos: int) -> None
        delete_by_node(self, target_node: any) -> None
        delete_head(self) -> None
        delete_tail(self) -> None
        get_data(self) -> any
        get_next(self) -> LinkedList | None
        has_next(self) -> bool
        insert(self, pos: int, data: any) -> None
        insert_head(self, data: any) -> None
        insert_tail(self, data: any) -> None
        set_data(self, data) -> None
        set_next(self, next) -> None
Function:
    get_linked_list(data: list) -> LinkedList
"""

from __future__ import annotations

import copy
from typing import Generator


def linked_list(data: list) -> LinkedList:
    """Return a linked list from a list"""
    if len(data) == 0:
        return LinkedList()
    else:
        head = LinkedList()
        head.set_data(data[0])
        node = head
        for value in data[1:]:
            new_node = LinkedList()
            new_node.set_data(value)
            node.set_next(new_node)
            node = node.get_next()
    return head


class LinkedList:
    """Class that represents a singly linked list"""

    def __init__(self) -> None:
        self.__data = None
        self.__next = None

    def __iter__(self) -> Generator[any, None, None]:
        node = self
        while node is not None:
            yield node.get_data()
            node = node.get_next()

    def __eq__(self, target_list: LinkedList) -> bool:
        if isinstance(target_list, LinkedList):
            if self.get_data() == target_list.get_data():
                if self.get_next() == target_list.get_next():
                    return True
        return False

    def __len__(self) -> int:
        count = 0
        node = self
        while 1:
            count += 1
            if node.get_next() is None:
                break
            node = node.get_next()
        return count

    def __repr__(self) -> LinkedList:
        return 'LinkedList()'

    def __str__(self) -> str:
        str_node = str(self.get_data())
        node = self
        while node.get_next() is not None:
            node = node.get_next()
            str_node = f'{str_node} -> {node.get_data()}'
        return str_node

    def clear(self) -> None:
        """Remove all nodes"""
        self.set_data(None)
        self.set_next(None)

    def delete_by_data(self, data: any) -> None:
        """Delete first occurence of a node with a specific value of data"""
        if self.get_data() == data:
            self.delete_head()
        else:
            node = self
            while node.get_next() is not None:
                if node.get_next().get_data() == data:
                    node.set_next(node.get_next().get_next())
                    break
                node = node.get_next()

    def delete_by_index(self, pos: int) -> None:
        """
        Delete a node in a specific position"""
        if pos < 0 or pos >= len(self):
            pass
        elif pos == 0:
            self.delete_head()
        elif pos == len(self):
            self.delete_tail()
        else:
            node = self
            count = 0
            while node.get_next() is not None:
                if pos-1 == count:
                    node.set_next(node.get_next().get_next())
                    break
                node = node.get_next()
                count += 1

    def delete_by_node(self, target_node: any) -> None:
        """Delete first occurence of a specific node"""
        if self == target_node:
            self.delete_head()
        else:
            node = self
            while node.get_next() is not None:
                if node.get_next() == target_node:
                    node.set_next(node.get_next().get_next())
                    break
                node = node.get_next()

    def delete_head(self) -> None:
        """Delete the head"""
        if len(self) == 1:
            return
        self.__class__ = self.__next.__class__
        self.__dict__ = self.__next.__dict__

    def delete_tail(self) -> None:
        """Delete the tail"""
        if len(self) == 2:
            if self.__next.next is None:
                self.__next = None
        else:
            node = self
            while 1:
                node = node.get_next()
                if node.get_next().next is None:
                    node.set_next(None)
                    break

    def get_data(self) -> any:
        """Get data field of the node"""
        return self.__data

    def get_next(self) -> LinkedList | None:
        """Get next field of the node"""
        return self.__next

    def has_next(self) -> bool:
        """Return True if the node points to another node"""
        return self.__next is not None

    def insert(self, pos: int, data: any) -> None:
        """
        Insert a new node in a specific position."""
        if pos < 0 or pos >= len(self):
            pass
        elif pos == 0:
            self.insert_head(data)
        elif pos == len(self):
            self.insert_tail(data)
        else:
            node = self
            count = 0
            while node.get_next() is not None:
                node = node.get_next()
                if pos-1 == count:
                    tmp = copy.deepcopy(node)
                    node.set_data(data)
                    node.set_next(tmp)
                    break
                count += 1

    def insert_head(self, data: any) -> None:
        """Insert a new head"""
        new_node = LinkedList()
        new_node.set_data(data)
        new_node.set_next(copy.deepcopy(self))
        self.__class__ = new_node.__class__
        self.__dict__ = new_node.__dict__

    def insert_tail(self, data: any) -> None:
        """Insert a new tail"""
        node = self
        while node.get_next() is not None:
            node = node.get_next()
        node.set_next(LinkedList())
        node.get_next().set_data(data)

    def set_data(self, data) -> None:
        """Set data field of the node"""
        self.__data = data

    def set_next(self, next) -> None:
        """Set next field of the node"""
        self.__next = next


if __name__ == '__main__':
    pass
