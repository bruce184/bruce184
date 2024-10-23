#include <bits/stdc++.h>
using namespace std;


string convert(int num){
    string dayName;

    // Using if statements for this is very inefficient
    // Use Switch statement

    switch (num){
    case 0:
        dayName = "Sunday";
        break; // break us out the switch statement, otherwise it will continue even when it found the right one
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        cout<<"The number is not valid.";
    }


    return dayName;
}


int main(){
    int n; cin>>n;

    cout<<convert(n)<<endl;

    return 0;
}
