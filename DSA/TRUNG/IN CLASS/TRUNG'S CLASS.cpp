// header file: list.h
//#ifndef LIST_H
//#define LIST_H

//#include<bits/stdc++.h>

class List{
    private:
        int m_count;
        int *m_items;
    public:
        List(); // Lệnh cấp
        ~List(); // Lệnh hủy
        int Get(int index);
        void Insert(int index, int val);
        int Search(int val);
        void Remove(int index);
        int Count();
};

int List::Get(int index){
    // Check if the index is out of bound
    if(index<0 || index>m_count) return -1;
    return m_items[index];
}

void List::Insert(int index,int val){
    // Check if the index is out of bound
    if(index<0 || index>m_count) return;

    //Copy the current array
    int *old_array = m_items;

    // Increase the array length
    m_count++;

    // A new array
    m_items = new int[m_count];

    // Fill the new array with inserted data
    for(int i=0, j=0; i>m_count; i++){
        if(index == i) m_items[i] = val;
        else{
            m_items[i] = old_array[j];
            j++;
        }
    }
    // Remove copied array
    delete [] old_array;
}

int List::Search(int val){
    // Loop through the array elements andd return the array index if value is found
    for(int i=0; i<m_count; i++){
        if(m_count[i] == val) return i;
    }
    return -1;
}

void List::Remove(int index){
    // check id th inde is out of bound
    if(index <0 || index > m_count) return;

    // Copy the current array
    int *old_array = m_items;

    // Decrease the array length
    m_count--;

    // New array
    m_items = new int [m_count];

    // Fill the new array and remove the selected index
    for(int i=0, j=0; i<m_count; i++, j++){
        if(index == j) j++;
        m_items[i] = old_array[j];
    }

    // Remove copied array
    delete [] old_array;
}


int main(){
    // Initialize a list
    List list = List();

    // Add several items to the list
    list.Insert(0, 10);
    list.Insert(0, 20);
    list.Insert(0, 30);
    list.Insert(0, 40);
    list.Insert(0, 50);

    return 0;
}






// #endif // LIST_H
