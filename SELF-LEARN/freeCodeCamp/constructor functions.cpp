#include <iostream>
using namespace std;

class Book{
    public: // to specify some attributes
        string title;
        string author;
        int pages;
        /*Book(string name){    // a constructor
            cout<<"Creating object"<<endl; // print out every time a NEW INSTANCE IS CREATED
            cout<<name<<endl;
        }*/
        // automatically solution
        Book(string aTitle, string aAuthor, int aPages){
            title = aTitle;
            author = aAuthor;
            pages = aPages;
        }

        Book(){
            title = "no Title";
            author = "no author";
            pages = 0;
        }

};

/* A constructor is a special function
    that is going to get called whenever we create an object of a class
    there can be many constructors in a class
*/

int main(){
    /*Book book1("Harry Potter"); // instance 1
    book1.title = "Harry Potter";
    book1.author = "JK Rowling ";
    book1.pages = 500;


    Book book2("Lord of the Rings"); // instance 2
    book2.title = "LOTR";
    book2.author = "Tolkein";
    book2.pages = 700;

    */

    // From 8 lines to 4 lines of code
    Book book1("Harry Potter", "JK Rowling", 500);
    Book book2("Lord of the Rings", "Tolkein", 700);
    Book book3;

    cout<<book3.title;

    return 0;
}

