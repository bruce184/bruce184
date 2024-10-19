#include <bits/stdc++.h>
using namespace std;

int main(){
    int age;
    cout<<"Please enter your age: ";
    cin>>age;

    cout<<"You are "<<age<<" years old."<<endl;

    // depend on the data type, it return that type

    // this is 2 separate block of code

    string name;
    cout<<"Enter your name: ";
    getline(cin, name); // get the whole line of text: the input prompt, variable to store in
    cout<<"Hello "<<name<<endl;

    return 0;
}
