#include <iostream>
#include <numeric>
#include <vector>
using namespace std;


int main(){
    int t; cin>>t;

    while (t--){
        int n, k; cin>>n>>k;
        vector<int>a(n);
        for(int i=0; i<n; i++){
            cin>>a[i];
        }

        bool check = false;

        for (int x=0; x<=n; x++){
            int dem = 0;
            for (int i=0; i<n; i++){
                if (a[i] <= x){
                    dem++;
                }
            }
            if(dem == k) check = true;
        }
        if (check) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
