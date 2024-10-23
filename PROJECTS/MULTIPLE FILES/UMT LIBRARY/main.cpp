#include <iostream>
using namespace std;

// Class Node
template <typename T>
class Node {
	public:
		T Value;
		Node<T> * Next;

		Node(T value);
};

template <typename T>
Node<T>::Node(T value): Value(value), Next(NULL){}

// Class LinkedList
template <typename T>
    class LinkedList{
        private:
            int m_count;

        public:
            // The first node in the list or null if empty
            Node<T> *Head;

            // The last node in the list or null if empty
            Node<T> *Tail;

            // Constructor
            LinkedList();

            // Get() operation
            Node<T> *Get(int index);


        // Get the value of the 2nd index
        // It should be 43
    cout<<"Remove value of index = 2"<<endl;
    Node<int> * get = linkedList.Get(2);
    if(get != NULL){
        cout<<get -> value;
    } else{
        cout<<"Not found";
    }
    cout<<endl<<endl;

        // Find the position of value 15
        // It must be 3
    cout<<"The position of value 15:"<<endl;
    int srch = linkedList.Search(15);
    cout<<srch<<endl<<endl;

        // Remove the 1st element
    cout<<"Remove the first element:"<<endl;
    linkedList.Remove(0);
        // 76 -> 43 -> 15 -> 48 -> 44 -> 100 -> NULL
    linkedList.PrintList();
    cout<<endl;

        // Remove the 5th element
    cout<<"Remove the fith element:"<<endl;
    linkedList.Remove(4);
        // 76 -> 43 -> 15 -> 48 0> 100 -> NULL
    linkedListed.PrintList();
    cout<<endl;

        // Remove the 10th element
    cout<<"Remove the tenth element:"<<endl;
    linkedList.Remove(9);
        // Nothing happened
        // 76 -> 43 -> 15 -> 48 -> 100 -> NULL
    linkedList.PrintList();
    cout<<endl;

return 0;
}
