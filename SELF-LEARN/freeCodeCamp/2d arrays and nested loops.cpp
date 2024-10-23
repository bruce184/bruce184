#include <bits/stdc++.h>
using namespace std;


int main(){
    int numGrid[3][2] ={   // prefer to specify
                    {1, 2},
                    {3, 4},
                    {5, 6}
    };

    cout<<numGrid[2][1]<<endl;

    for (int i=0; i<3; i++){
        for (int j=0; j<2; j++){
             cout<<numGrid[i][j]<<" ";
        }
    cout<<endl;
    }

    return 0;
}
