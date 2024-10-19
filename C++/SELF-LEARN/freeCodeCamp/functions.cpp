#include <bits/stdc++.h>
using namespace std;
// Define Functions before the main function
// or Declare it first
    // void function: returns nothing
void sayHi(string name, int age);


// this is the MAIN FUNCTION: all the code inside this function will be executed
int main(){

    sayHi("Mike", 60); // CALL the function

    return 0;
}

// void function: returns nothing
void sayHi(string name, int age){ // pass into parameters
    cout<<"Hello "<<name<<", you are "<<age<<endl;
}

