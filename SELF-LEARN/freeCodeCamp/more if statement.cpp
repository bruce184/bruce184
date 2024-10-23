#include <bits/stdc++.h>
using namespace std;


int getMax(int num1, int num2, int num3){
    int res;

    if (num1 > num2 && num1 > num3){
        res = num1;
    } else if (num2 > num1 && num2 > num3) {
        res = num2;
    } else res = num3;

    return res;
}


int main(){
    int n1, n2, n3; cin>>n1>>n2>>n3;

    int ans = getMax(n1, n2, n3);
    cout<<"The bigger number is: "<<ans<<endl;

    return 0;
}
