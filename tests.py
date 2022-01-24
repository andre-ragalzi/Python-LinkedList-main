import unittest

import linked_list as llist


class TestLinkedList(unittest.TestCase):
    def test_clear(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        llist2 = llist.LinkedList()
        self.assertEqual(llist1, llist.LinkedList(0, 1, 2, 3))
        self.assertEqual(len(llist1), 4)
        self.assertEqual(llist2, llist.LinkedList())
        self.assertEqual(len(llist2), 0)
        llist1.clear()
        llist2.clear()
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        self.assertEqual(llist2, llist.LinkedList())
        self.assertEqual(len(llist2), 0)

    def test_delete_by_index(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        self.assertRaises(ValueError, llist1.delete_by_index, 8)
        llist1.delete_by_index(1)
        self.assertEqual(llist1, llist.LinkedList(0, 2, 3))
        self.assertEqual(len(llist1), 3)
        llist1.delete_by_index(0)
        self.assertEqual(llist1, llist.LinkedList(2, 3))
        self.assertEqual(len(llist1), 2)
        llist1.delete_by_index(1)
        self.assertEqual(llist1, llist.LinkedList(2))
        self.assertEqual(len(llist1), 1)
        llist1.delete_by_index(0)
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        self.assertRaises(ValueError, llist1.delete_by_index, 1)

    def test_delete_by_node(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        node0 = llist.Node(0)
        node1 = llist.Node(1)
        node2 = llist.Node(2)
        node3 = llist.Node(3)
        llist1.delete_by_node(node1)
        self.assertEqual(llist1, llist.LinkedList(0, 2, 3))
        self.assertEqual(len(llist1), 3)
        # delete a non exists node
        self.assertRaises(ValueError, llist1.delete_by_node, node1)
        self.assertEqual(len(llist1), 3)
        llist1.delete_by_node(node3)
        self.assertEqual(llist1, llist.LinkedList(0, 2))
        self.assertEqual(len(llist1), 2)
        llist1.delete_by_node(node0)
        self.assertEqual(llist1, llist.LinkedList(2))
        self.assertEqual(len(llist1), 1)
        llist1.delete_by_node(node2)
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        # delete from empty llist
        self.assertRaises(ValueError, llist1.delete_by_node, node1)

    def test_delete_by_value(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        llist1.delete_by_value(1)
        self.assertEqual(llist1, llist.LinkedList(0, 2, 3))
        self.assertEqual(len(llist1), 3)
        # delete a non exists value
        self.assertRaises(ValueError, llist1.delete_by_value, 1)
        llist1.delete_by_value(3)
        self.assertEqual(llist1, llist.LinkedList(0, 2))
        self.assertEqual(len(llist1), 2)
        llist1.delete_by_value(0)
        self.assertEqual(llist1, llist.LinkedList(2))
        self.assertEqual(len(llist1), 1)
        llist1.delete_by_value(2)
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        # delete from empty llist
        self.assertRaises(ValueError, llist1.delete_by_value, 1)
        self.assertEqual(len(llist1), 0)

    def test_delete_head(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        llist1.delete_head()
        self.assertEqual(llist1, llist.LinkedList(1, 2, 3))
        self.assertEqual(len(llist1), 3)
        llist1.delete_head()
        self.assertEqual(llist1, llist.LinkedList(2, 3))
        self.assertEqual(len(llist1), 2)
        llist1.delete_head()
        self.assertEqual(llist1, llist.LinkedList(3))
        self.assertEqual(len(llist1), 1)
        llist1.delete_head()
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        self.assertRaises(ValueError, llist1.delete_head)
        self.assertEqual(len(llist1), 0)

    def test_delete_tail(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        llist1.delete_tail()
        self.assertEqual(llist1, llist.LinkedList(0, 1, 2))
        self.assertEqual(len(llist1), 3)
        llist1.delete_tail()
        self.assertEqual(llist1, llist.LinkedList(0, 1))
        self.assertEqual(len(llist1), 2)
        llist1.delete_tail()
        self.assertEqual(llist1, llist.LinkedList(0))
        self.assertEqual(len(llist1), 1)
        llist1.delete_tail()
        self.assertEqual(llist1, llist.LinkedList())
        self.assertEqual(len(llist1), 0)
        self.assertRaises(ValueError, llist1.delete_tail)
        self.assertEqual(len(llist1), 0)

    def test_insert(self):
        llist1 = llist.LinkedList(0, 1, 2, 3)
        llist1.insert(2, 99)
        self.assertEqual(llist1, llist.LinkedList(0, 1, 99, 2, 3))
        self.assertEqual(len(llist1), 5)
        llist1.insert(0, 100)
        self.assertEqual(llist1, llist.LinkedList(100, 0, 1, 99, 2, 3))
        self.assertEqual(len(llist1), 6)
        llist1.insert(6, 101)
        self.assertEqual(llist1, llist.LinkedList(100, 0, 1, 99, 2, 3, 101))
        self.assertEqual(len(llist1), 7)
        self.assertRaises(ValueError, llist1.insert, 10, 102)
        self.assertEqual(len(llist1), 7)

    def test_insert_head(self):
        llist1 = llist.LinkedList(0, 1)
        llist1.insert_head(100)
        self.assertEqual(llist1, llist.LinkedList(100, 0, 1))
        self.assertEqual(len(llist1), 3)
        llist1.clear()
        llist1.insert_head(100)
        self.assertEqual(llist1, llist.LinkedList(100))
        self.assertEqual(len(llist1), 1)

    def test_insert_tail(self):
        llist1 = llist.LinkedList(0, 1)
        llist1.insert_tail(100)
        self.assertEqual(llist1, llist.LinkedList(0, 1, 100))
        self.assertEqual(len(llist1), 3)
        llist1.clear()
        llist1.insert_tail(100)
        self.assertEqual(llist1, llist.LinkedList(100))
        self.assertEqual(len(llist1), 1)


if __name__ == '__main__':
    unittest.main()
