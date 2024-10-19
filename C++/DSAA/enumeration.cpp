/* Leveraging the variable capability using advanced data types
	ENUMERATION
Use case: Creat a program that generates a random card
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

enum CardSuits{
	Club,
	Diamond,
	Heart,
	Spade
};

enum CardElements{
	Ace,
	Two,
	Three,
	Four,
	Five,
	Six,
	Seven,
	Eight,
	Nine,
	Ten,
	Jack,
	Queen,
	King
};

string GetSuitsString(CardSuits suit){
	string s;
	switch(suit){
		case Club:
			s = "Club"; break;
		case Diamond:
			s = "Diamond"; break;
		case Heart:
			s = "Heart"; break;
		case Spade:
			s = "Spade"; break;
	}
	return s;
}

string GetElementsString(CardElements element){
	string e;
	switch(element){
		case Ace:
			e = "Ace"; break;
		case Two:
			e = "Two"; break;
		case Three:
			e = "Three"; break;
		case Four:
			e = "Four"; break;
		case Five:
			e = "Five"; break;
		case Six:
			e = "Six"; break;
		case Seven:
			e = "Seven"; break;
		case Eight:
			e = "Eight"; break;
		case Nine:
			e = "Nine"; break;
		case Ten:
			e = "Ten"; break;
		case Jack:
			e = "Jack"; break;
		case Queen:
			e = "Queen"; break;
		case King:
			e = "King"; break;
	}
	return e;
}

int GenerateRandomNumber(int min, int max){
	static const double fraction = 1. / (static_cast<double>(RAND_MAX) + 1.);
	return min + static_cast<int>((max-min+1) * (rand()*fraction));
}

int main(){
	// set initial seed value to system clock
	srand(static_cast<unsigned int>(time(0)));

	// generate random suit and element card
	int iSuit = GenerateRandomNumber(0,3);
	int iElement = GenerateRandomNumber(0,12);

	CardSuits suit = static_cast<CardSuits>(iSuit);
	CardElements element = static_cast<CardElements>(iElement);

	cout<<"Your card is " <<GetElementsString(element)<<" of "<<GetSuitsString(suit)<<endl;
return 0;
}
