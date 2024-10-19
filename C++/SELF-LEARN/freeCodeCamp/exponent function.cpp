#include <bits/stdc++.h>
using namespace std;

int power(int baseNum, int powNum){
    int res =1;
    for (int i=0; i<powNum; i++){
        res = res * baseNum;
    }
    return res;
}

int main(){

   cout<<pow(2, 3);

    return 0;
}
