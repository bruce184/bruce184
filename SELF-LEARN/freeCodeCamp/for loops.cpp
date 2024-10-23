#include <bits/stdc++.h>
using namespace std;


int main(){
    // Comparison to while loops
    int index = 1;
    while (index <= 5){ // usually called "looping guard"
        cout<<index<<endl; // 1 2 3 4 5
        index++;
    }

    // For loops use indexing variables; more conditions in the parentheses -> shorter syntax
    for (int i=0; i<=5; i++){
        cout<<index<<endl; // 1 2 3 4 5
    }

    int num[] = {1, 2, 5, 7, 3};
    for (int i=0; i<5; i++){
        cout<<num[i]<<endl;
    }

    return 0;
}
