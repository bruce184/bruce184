#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct Employee{
    char name[50];
    float salary;
    int age;
    int id;
};
struct Employee e;

void addRecord(fstream &file);
void deleteRecord(fstream &file);
void displayRecords(fstream &file);
void modifyRecord(fstream &file);

//File stream objects


// MAIN Code
int main(){
    // Opening the file
    fstream file("data.txt", ios::in | ios::out | ios::binary);

    // Checking if file is successfully opened
    if(!file){
        cerr<<"Cannot open file"<<endl;
        exit(1); // CHƯA HIỂU
    }

    // Biểu hiện menu lựa chọn
    int choice;
    while (true){
        cout<<"1. Add Record"<<"          "<<"2. Delete Record"<<endl;
        cout<<"3. Dislay Records"<<"      "<<"4. Modify Record"<<endl;
        cout<<"5. Exit"<<endl;
        cout<<endl;
        cout<<"Enter your choice: "<<endl;
        cin>>choice;


    // Hàm để nhận dạng và chạy mỗi trường hợp chọn
    switch(choice){
        case 1: addRecord(file);
        break;
        case 2: deleteRecord(file);
        break;
        case 3: displayRecords(file);
        break;
        case 4: modifyRecord(file);
        break;
        case 5: file.close();
        exit(0);
        default:
            cout<<"Invalid choice. Please try again."<<endl;
    }
}
return 0;
}


//Function 1
void addRecord(fstream &file){
    file.seekp(0, ios::end); //CHƯA HIỂU

    char choice = 'y';

    Employee e;
    while(choice == 'y' || choice == 'Y'){
        cout<<"Your name: "<<endl;
        cin>>e.name;
        cout<<"Age: "<<endl;
        cin>>e.age;
        cout<<"Salary: "<<endl;
        cin>>e.salary;
        cout<<"ID: "<<endl;
        cin>>e.id;

        file.write(reinterpret_cast<char *>(&e), sizeof(e)); //CHƯA HIỂU

        cout<<"Do you want to add another record (Y/N): ";
        cin>>choice;
    }
}

// Function 2
void deleteRecord(fstream &file){
    string empName;
    char choice = 'y';

    while(choice == 'y' || choice == 'Y'){
        cout<<"Enter the employee's name to delete: "<<endl;
        cin>>empName;

        fstream temp("temp.txt", ios::out | ios::binary); //CHƯA HIỂU

        Employee e;
        while(file.read(reinterpret_cast<char *>(&e), sizeof(e))){ //CHƯA HIỂU
            if(e.name != empName){
                temp.write(reinterpret_cast<char *>(&e), sizeof(e)); //CHƯA HIỂU
            }
        }

        temp.close(); //CHƯA HIỂU
        file.close(); //CHƯA HIỂU
        remove("data.txt"); //CHƯA HIỂU
        rename("temp.txt", "data.txt"); //CHƯA HIỂU

        file.open("data.txt", ios::in | ios::out | ios::binary); //CHƯA HIỂU

        cout<<"Do you want to delete another record (Y/N): "<<endl;
        cin>>choice;

    }
}

// Function 3
void displayRecords(fstream &file){
    system("cls");

    cout<<"============================="<<endl;
    cout<<"Name: "<<endl<<"Age: "<<endl<<"Salary: "<<endl<<"ID: "<<endl;
    cout<<"============================="<<endl;

    file.seekg(0, ios::beg);

    Employee e;
    while (file.read(reinterpret_cast<char *>(&e), sizeof(e))) {
        cout << e.name << "\t" << e.age << "\t" << e.salary << "\t" << e.id << endl;
    }

    cout<<endl;
    system("pause"); // CHƯA HIỂU
}

// Function 4
void modifyRecord(fstream &file){
    string empName;
    char choice = 'y';

    while(choice == 'y' || choice == 'Y'){
        cout<<"Enter the employee's name to modify: "<<endl;
        cin>>empName;

        file.seekg(0, ios::beg);

        Employee e;
        while(file.read(reinterpret_cast<char *>(&e), sizeof(e))){
            if(e.name == empName){
                cout<<"Enter new name: "<<endl;
                cin>>e.name;
                cout<<"Enter new age: "<<endl;
                cin>>e.age;
                cout<<"Enter new salary: "<<endl;
                cin>>e.salary;
                cout<<"Enter new ID: "<<endl;
                cin>>e.id;

                file.seekp(file.tellg() - sizeof(e), ios::beg);
                file.write(reinterpret_cast<char *>(&e), sizeof(e));

                break;
                }
        }
        cout<<"Do you want to modify another record (Y/N): ";
        cin>>choice;
    }
}
