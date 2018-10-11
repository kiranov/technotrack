from list import DoubleLinkedList 
import pytest

class TestList:
	
	def test_push_pop_one(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(2)
		db.push(3)
		assert(list([db.pop(), db.pop(), db.pop()]) == [3, 2, 1])
		
	def test_push_two(self):
		db = DoubleLinkedList()
		db.push(1)
		assert(list([db.pop()]) == [1])
		
	def test_push_three(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(2)
		db.push(3)
		assert(list([db.len()]) == [3])
		
		
	def test_len_one(self):
		db = DoubleLinkedList()
		db.push(1)
		assert(list([db.len()]) == [1])
		
	def test_len_two(self):
		db = DoubleLinkedList()
		db.push(1)
		db.pop()
		assert(list([db.len()]) == [0])
		
	def test_len_three(self):
		db = DoubleLinkedList()
		assert(list([db.len()]) == [0])
		
	def test_shift_unshift_one(self):
		db = DoubleLinkedList()
		db.unshift(1)
		db.unshift(2)
		db.unshift(3)
		assert(list([db.shift(), db.shift()]) == [3, 2])
		
	def test_shift_two(self):
		db = DoubleLinkedList()
		db.push(1)
		assert(list([db.shift()]) == [1])
		
	def test_shift_three(self):
		db = DoubleLinkedList()
		assert(list([db.shift()]) == [None])
		
	def test_delete_one(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(2)
		db.push(1)
		db.push(3)
		db.push(4)
		db.delete(1)
		assert(list([db.shift(), db.shift(), db.shift()]) == [2, 3, 4])
		
	
	def test_delete_two(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(1)
		db.push(1)
		db.push(1)
		db.push(1)
		db.delete(1)
		assert(list([db.pop()]) == [None])
		
		
	def test_delete_three(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(2)
		db.push(3)
		db.push(4)
		db.push(5)
		db.delete(8)
		assert(list([db.shift(), db.shift(), db.shift(), db.shift(), db.shift()]) == [1, 2, 3, 4, 5])
		
	def test_contains(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(2)
		db.push(3)
		db.push(4)
		db.push(5)
		assert(list([db.contains(4)]) == [True])
		
	def test_contains2(self):
		db = DoubleLinkedList()
		db.push(1)
		db.push(1)
		db.push(1)
		db.push(1)
		db.push(1)
		assert(list([db.contains(1), db.contains(2)]) == [True, False])
	
	def test_contains3(self):
		db = DoubleLinkedList()
		assert(list([db.contains(2)]) == [False])
