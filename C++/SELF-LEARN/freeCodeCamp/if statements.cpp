#include <bits/stdc++.h>
using namespace std;

int main(){
    bool isMale = true;
    bool isTall = false;

    // if 1 one them is false, the whole is false
    /*
    if(isMale && isTall){
        cout<<"You are a tall male"<<endl;
    } else {
        cout<<"You are not male and short"<<endl;
    }
    */

    // because 1 of them is True so this is True
    /*
    if(isMale || isTall){
        cout<<"You are a tall male"<<endl;
    } else {
        cout<<"You are not male and short"<<endl;
    }
    */


    if(isMale && isTall){ // have both
        cout<<"You are a tall male"<<endl;
    } else if(isMale && !isTall) { // is male but not tall
        cout<<"You are a male but short"<<endl;
    } else if (!isMale && isTall){ // not male but tall
        cout<<"You are tall but not male."<<endl;
    } else { // not both
        cout<<"You are not male and not tall."<<endl;
    }


    return 0;
}
