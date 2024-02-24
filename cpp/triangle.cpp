#include <iostream>
#include <cmath>
using namespace std;

class Triangle{
	double a, b, c;

public:
	Triangle(double latoa,double latob,double latoc){
		a = latoa; b = latob; c = latoc;
	}
	double perimeter(){
		double p;
		p = ((a+b+c)/2);
		return p;
	}

	double area(){
		double are, p;
		p = ((a+b+c)/2);
		are = sqrt(p*(p-a)*(p-b)*(p-c)); 
		return are;
		
	}

};


int main(){
	double latoa, latob, latoc, p_tri, a_tri;
	
	cout << "Inserisci i lari a, b, c del triangolo\n";
	cin >> latoa >> latob >> latoc;
	
	Triangle t = Triangle(latoa,latob,latoc);
	
	p_tri = t.perimeter();
	a_tri = t.area();
	cout << "Perimetro del triangolo: " << p_tri << "\n";
	cout << "Area del triangolo: " << a_tri << "\n";
}
