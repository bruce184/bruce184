#include <bits/stdc++.h>
using namespace std;

int main(){

    cout<<"Giraffe Academy\n"; // "\n" is the same as "endl" - print a new empty line after this line
    cout<<"Hello"<<endl;
    cout<<endl;

    // string functions: a block of code that perform a specific task
    string phrase = "F4";
    cout<<phrase.length()<<endl; // string function: length()
    cout<<phrase[0]<<endl;
    cout<<phrase[1]<<endl;
    cout<<phrase[2]<<endl;

    // change the value of a index
    phrase[3] = 'F';
    cout<<phrase[3]<<endl;

    cout<<phrase.find("Academy",0); // the value wanted to search, the starting search index of that whole string
    cout<<phrase.substr(8, 3)<<endl; // create a new string from the original: the starting idx and the length
    string phrasesub = phrase.substr(8,3);
    cout<<phrasesub;

    return 0;
}
