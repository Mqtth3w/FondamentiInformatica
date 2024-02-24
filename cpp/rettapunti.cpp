#include <iostream>
#include <cmath>
using namespace std;

class Segmenti{
	double x1, y1, x2, y2;

public:
	Segmenti(double p1x,double p1y,double p2x,double p2y){
		x1 = p1x; y1 = p1y; x2 = p2x; y2 = p2y;
	}
	double slope(){
		double m;
		m = (y2-y1) / (x2-x1);
		return m;
	}

	double intercept(){
		double quota_orig, m;
		m = (y2-y1) / (x2-x1);
		quota_orig = y1-(m*x1);
		return quota_orig;
		
	}
	
};


int main(){
	double p1x, p1y, p2x, p2y, coef, q_orig;
	
	
	cout << "Inserisci le coordinate x, y del primo punto\n";
	cin >> p1x >> p1y;
	cout << "Inserisci le coordinate x, y del secondo punto\n";
	cin >> p2x >> p2y;
	
	Segmenti s = Segmenti(p1x,p1y,p2x,p2y);
	
	coef = s.slope();
	q_orig = s.intercept();
	cout << "Coefficente angolare: " << coef << "\n";
	cout << "Ordinata all'origine: " << q_orig << "\n";
}
