#include <iostream>
#include <vector>
using namespace std;

int main (){
	vector<double> valori, sotto, sopraug;
	double media, res, sum;
	
	cout << "inserisci un numero reale positivo?\n";
	cin >> res;
	while (res > 0){
		valori.push_back(res);
		sum += res;
		cout << "inserisci un numero reale positivo?\n";
		cin >> res;
	}
	media = sum/valori.size();
	for (int i=0; i<valori.size(); ++i){
		if ( valori[i] < media){
			sotto.push_back(valori[i]);
		}
		else {
			sopraug.push_back(valori[i]);
		}
	}
	
	cout << "media dei valori: " << media << "\n";
	cout << "valori sotto la media: ";
	for (auto n: sotto){
		cout << n << " ";
	}
	cout << "\n" << "valori maggiori o uguali alla media: ";
	for (auto m: sopraug){
		cout << m << " ";
	}
}