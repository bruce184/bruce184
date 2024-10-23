#include <iostream>
using namespace std;
/* Classes and objects are very important
    Some objects can be represented by variables
        string name = "Bruce";
        double pi = 3.14;
        char favoriteLetter = 'G';
    But in reality, there're many entities can not be represented by a simple variable, for example: a book
    => Use classes

    A class is essentially a blueprint/template of a new data type -> define a new data type
        an object is an INSTANCE OF THAT TEMPLATE
*/

class Book{
    public: // to specify some attributes
        string title;
        string author;
        int pages;
};



int main(){
    Book book1;
    book1.title = "Harry Potter";
    book1.author = "JK Rowling";
    book1.pages = 500;

    cout<<book1.title;

    return 0;
}
