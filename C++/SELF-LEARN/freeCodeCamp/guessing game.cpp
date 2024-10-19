#include <bits/stdc++.h>
using namespace std;



int main(){
    int secretNum = 7;
    int guess;
    int guesscount = 0;
    int guesslimit = 3;
    bool outofGuess = false;

    while(guess != secretNum && !outofGuess){
        if (guesscount < guesslimit){
            cout<<"Enter guess: ";
            cin>>guess;
            guesscount++;
        } else {
            outofGuess = true;
        }
    }

    if (outofGuess == true){
        cout<<"You lose!"<<endl;
    } else cout<<"You win!"<<endl;

    return 0;
}
