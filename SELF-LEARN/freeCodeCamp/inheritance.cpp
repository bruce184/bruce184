#include <iostream>
using namespace std;

class Chef(){
    public:
        void makeChicken(){
            cout<<"The chef makes chckien"<<endl;
        }
        void makeSalad(){
            cout<<"The chef makes salad"<<endl;
        }
        void makeSpecialDish(){
            cout<<"The chef makes bbq"<<endl;
        }
};


class ItalianChef: public Chef{
    public:
        void makePasta(){
            cout<<"The chef makes pasta"<<endl;
        }

};


int main(){
    Chef chef;
    chef.makeSalad();

    ItalianChef italianChef;
    italianChef.makePasta();

    return 0;
}
