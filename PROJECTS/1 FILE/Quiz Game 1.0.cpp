#include <iostream>
#include <string>

using namespace std;



//Question Class
class Question{
private:
    string Question_text;
    string Answer_1;
    string Answer_2;
    string Answer_3;
    string Answer_4;
    char Correct_Answer;
    int Question_Score;

public:
    void setValues(string, string, string, string, string, char, int);
    void askQuestion();

};

char Guess;
int Total = 0;

int main(){
// Intro
    cout<<"DAILY QUIZ"<<endl;
    cout<<"Press Enter to start "<<endl;

    cin.get(); // Để có chức năng Bấm Enter

// Input the details
string Name;
int Age;

    cout<<"What is your name: "<<endl;
    cin>>Name;

    cout<<endl;

    cout<<"How old are you: "<<endl;
    cin>>Age;

    cout<<endl;


// Ask the player
string Rep;
    cout<<"Are you ready to take"<<" the quiz "<<Name<<"?"<<endl<<"yes / no"<<endl;
    cin>>Rep;
    if(Rep == "yes"){
        cout<<endl<<"Good luck! "<<endl;
    }
    else {
        cout<<"OK. Good Bye!"<<endl;
    return 0; //chưa hiểu, nếu ko có thì vẫn hiện ra chạy game -> ĐỂ NGẮT CHƯƠNG TRÌNH nếu trả lời 'no'
    }

// Objects in the class
    Question q1;
    Question q2;
    Question q3;
    Question q4;
    Question q5;
    Question q6;
    Question q7;
    Question q8;
    Question q9;
    Question q10;

//when changing to the answer to letter, 'A' is the correct code not "A"
q1.setValues("1. What is admin's name? ", "Nguyen Huy Hoang", "Nguyen Hoang", "Vo Nguyen Huy Hoang", "Nguyen Minh Hoang", 'A', 10);
q2.setValues("2. Full birthdate? ", "08/11/2005", "03/03/2005", "22/07/2005", "01/11/2005", 'B', 10);
q3.setValues("3. Height? ", "1m9", "1m8", "1m7", "1m75", 'C', 10);
q4.setValues("4. Our solar system belongs to which galaxy?", "Zodiac Galaxy", "Starburst Galaxy", "Small Magellanic Cloud", "Milky Way Galaxy", 'D', 10);
q5.setValues("5. In 1954, which war concluded with the signing of the Geneva Accords? ", "World War II", "Cold War", "Korean War", "Vietnam War", 'D', 10);
q6.setValues("6. Which country is named after a famous mountain range? ", "Canada", "Jordan", "Nepal", "Peru", 'C', 10);
q7.setValues("7. Which mathematician from England, famous for naming his differential equation? ", "George Boole", "Isaac Newton", "Alan Turing", "Charles Babbage", 'B', 10);
q8.setValues("8. In literature, what is the name of the fictional detective created by Arthur Conan Doyle? ", "Sherlock Holmes", "Hercule Poirot", "Sam Spade", "Miss Marple", 'A', 10);
q9.setValues("9. Who is the founder of Naturalism and Taoism philosophy in China?","Fe","Francium", "Fluor", "Phosphorus", 'D', 10);
q10.setValues("10. In physics, what is the fundamental constant that relates a photon's energy to its frequency? ", "Boltzmann constant", "Avogadro's constant", "Planck's constant", "Speed of light", 'C', 10);


q1.askQuestion();
q2.askQuestion();
q3.askQuestion();
q4.askQuestion();
q5.askQuestion();
q6.askQuestion();
q7.askQuestion();
q8.askQuestion();
q9.askQuestion();
q10.askQuestion();


// Display the score -> Finish or Try again
    cout<<"Total score = "<<Total<<" out of 100"<<endl;

    cout<<endl;

    if(Total >=70){
        cout<<"Congrats "<<Name<<" you have passed the quiz"<<endl;
    }
    else {
        cout<<"Too bad, you have failed the quiz"<<endl;
        cout<<"Try again "<<endl;
    }
        return 0;
    }

//Function to set the values of the questions
void Question::setValues(string a, string b, string c, string d, string e, char f, int g){
    Question_text = a;
    Answer_1 = b;
    Answer_2 = c;
    Answer_3 = d;
    Answer_4 = e;
    Correct_Answer = f;
    Question_Score = g;
}

//Function to ask questions
void Question :: askQuestion(){
    cout<<endl;

    cout<<Question_text<<endl;
    cout<<"A. "<<Answer_1<<"            "<<"B. "<<Answer_2<<endl;
    cout<<"C. "<<Answer_3<<"            "<<"D. "<<Answer_4<<endl;
    cout<<endl;

// The answer player chooses
    cout<<"What is your answer?"<<endl;
    cin>>Guess;

    cout<<endl;

// IF RIGHT
    if(Guess == Correct_Answer){
        cout<<"Correct!"<<endl;
        cout<<"Score = 10"<<endl;
        //Update the score
        Total = Total + Question_Score;
        cout<<"Total score = "<<Total<<endl;

    }
// IF WRONG
    else {
        cout<<"Wrong"<<endl;
        cout<<"Score = 0"<<endl;
        Total = Total;
        cout<<"Total score = "<<Total<<endl;
        cout<<"Correct answer was "<<Correct_Answer<<endl;
    }
    cout<<"__________________________"<<endl;
}
