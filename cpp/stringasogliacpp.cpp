#include <iostream> 
#include <vector>
#include <string>
using namespace std;

double long_lines(int soglia, vector<string> lista){
	int numstr = 0;
	
    for (auto stringa: lista){
        if (stringa.size() >= soglia){
            ++numstr;
		}
	}
    return numstr;
}

int main() {
	string testo;
	int sogl, result;
	vector<string> listas;
	cout << "Digita una stringa di testo\n";
	getline(cin,testo);
	while (testo != ""){
		listas.push_back(testo);
		cout << "Digita una stringa di testo\n";
		getline(cin,testo);
	}
	cout << "Inserire una soglia\n";
	cin >> sogl;
    while (sogl > 0){
        result = long_lines(sogl, listas);
		cout << "Le stringhe maggiori della soglia sono: ";
		cout << result << "\n";
		cout << "Inserire una soglia\n";
        cin >> sogl;
	}
}