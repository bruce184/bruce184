#include <bits/stdc++.h>
using namespace std;

struct node {
    int data;
    node* left;
    node* right;
};
typedef node *Pnode;


double tong(Pnode t){
    double S = 0;
    if (t != NULL){
        S = t->data + tong(t->left) + tong(t->right);
    }
    return S;
}



int main(){

	return 0;
}
