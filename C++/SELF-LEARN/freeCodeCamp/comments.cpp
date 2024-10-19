#include <bits/stdc++.h>
using namespace std;

// Pointer: is a memory address, a type of data

int main(){
    int age = 19;
    string name = "Mike";
    double gpa = 2.7;

    // Print out the memory addresses of these variables
    cout<<"Age: "<<&age<<endl;;
    cout<<"Name: "<<&name<<endl;
    cout<<"GPA: "<<&gpa<<endl;

    // Create a pointer variable (with the same name of the one u want to store the address)
    //     a container for a pointer
    // &: ampersand for the original variable
    //  *: asterix for the pointer variable
    int *pAge = &age;
    double *pGPA = &gpa;

    cout<<pAge<<endl<<pGPA<<endl; // 0xc79b9ff9a0;  0xc79b9ff978

    // Dereferencing: get that value stored in that memory address, by using an asterix
    cout<<*pAge<<" "<<*pGPA<<endl; // 19;    2.7
    cout<<*&age<<endl;  // depend on the first symbol, it will execute on that one




    return 0;
}
