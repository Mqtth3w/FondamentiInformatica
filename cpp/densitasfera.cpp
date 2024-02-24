#include <iostream>
using namespace std;

double sphere_density(double massakg, double raggiom){
	double volume, ro, PI;
	PI = 3.1415926535897932384626433832795;
	volume = (4/3)*PI*(raggiom*raggiom*raggiom);
	ro = massakg/volume;
	return ro;
}	

int main (){
	double mkg, rm, result;
	cout << "massa in Kg?\n";
	cin >> mkg;
	cout << "raggio in metri?\n";
	cin >> rm;
	result = sphere_density(mkg, rm);
	cout << "densita della sfera: " << result;
}