#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

struct Question {
    string questionText;
    string answer1;
    string answer2;
    string answer3;
    string answer4;
    char correctAnswer;
    int questionScore;

    void askQuestion();
};

void Question::askQuestion() {
    cout << endl;
    cout << questionText << endl;
    cout << "A. " << answer1 << "            B. " << answer2 << endl;
    cout << "C. " << answer3 << "            D. " << answer4 << endl;
    cout << endl;

    char guess;
    cout << "What is your answer?" << endl;
    cin >> guess;

    if (toupper(guess) == correctAnswer) {
        cout << "Correct!" << endl;
        cout << "Score = " << questionScore << endl;
    } else {
        cout << "Wrong" << endl;
        cout << "Score = 0" << endl;
        cout << "Correct answer was " << correctAnswer << endl;
    }
    cout << "__________________________" << endl;
}

int main() {
    ifstream file("questions.txt");
    string line;
    vector<Question> questions;
    int totalScore = 0;

    // Read questions from file
    while (getline(file, line)) {
        stringstream ss(line);
        Question q;
        string score;
        getline(ss, q.questionText, ';');
        getline(ss, q.answer1, ';');
        getline(ss, q.answer2, ';');
        getline(ss, q.answer3, ';');
        getline(ss, q.answer4, ';');
        ss >> q.correctAnswer;
        ss.ignore();
        getline(ss, score);
        q.questionScore = stoi(score);
        questions.push_back(q);
    }

    // Continue with the rest of your program setup...
    for (auto& q : questions) {
        q.askQuestion();
        totalScore += q.questionScore;
    }

    // Output total score and other concluding messages...
    cout << "Total score = " << totalScore << " out of " << questions.size() * 10 << endl;
    // Additional code for player feedback...

    return 0;
}

