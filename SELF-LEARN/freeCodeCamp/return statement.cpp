#include <bits/stdc++.h>
using namespace std;
// when it comes to return, it will break off the code or the block of code

double cube(double num){
    // double res = num * num * num;
    // return res;
    return num * num * num;
    cout<<"Hello"; // doesn't print out because return above
}


int main(){

    double ans = cube(5.5);
    cout<<ans;

    return 0;
}
