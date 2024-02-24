#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool romo(string palind){
	if (palind.length() <= 1){
		return true;
	}
	
	if (palind[0] == palind[palind.length()-1] ){
		return romo(palind.substr(1, palind.length()-2));
	}
	else {return false;}
}

int main (){
	string palindromo;
	cout << "Stringa? \n";
	getline(cin, palindromo);
	bool result = romo(palindromo);
	if (result == true){
		cout << "La stringa è un palindromo";
	}
	else{
		cout << "La stringa non è un palindromo";
	}
}
