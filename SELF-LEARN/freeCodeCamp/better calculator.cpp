#include <bits/stdc++.h>
using namespace std;


int main(){
    int num1, num2, res;
    char op;

    cout<<"Enter 1st number: ";cin>>num1;
    cout<<"Enter the operator: "; cin>>op;
    cout<<"Enter second number: "; cin>>num2;

    if (op == '+'){
        res =  num1 + num2;
    } else if (op == '-'){
        res = abs(num1 - num2);
    } else if (op == '*'){
        res = num1 * num2;
    } else if (op == '/'){
        res = abs(num1/num2);
    } else cout<<"Please enter a valid operator!"<<endl;

    cout<<"Result = "<<res<<endl;

    return 0;
}
