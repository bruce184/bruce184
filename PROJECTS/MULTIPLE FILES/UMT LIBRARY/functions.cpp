#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>
#include "node.h"

using namespace std;

template <typename T>
class LinkedList{
	private:
		int m_count;

	public:
		// The first node in the list or null if empty
		Node<T> * Head;

		// The last node in the list or null if empty
		Node<T> * Tail;

		// Constructor
		LinkedList();

		// Get() operation
		Node<T> * Get(int index);

		// Insert() operation
		void insert_head(T val);
		void insert_tail(T val);
		void Insert(int index, T val);

		// Search() operation
		int Search(T val);

		// Remove() operation
		void remove_head();
		void remove_tail();
		void remove(int index);


