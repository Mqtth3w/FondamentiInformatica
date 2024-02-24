#include <iostream>
#include <vector>
#include "g2d\canvas.hpp"
using namespace std;

void tick(){
	int val, q;
	int dim = 500;
	int j=0;
	vector <int> lista;
	cout << "valore? " << "\n"; 
	cin >> val;
	while (0 < val && val < 255){
		lista.push_back(val);
		cout << "valore? " << "\n"; 
		cin >> val;
	}
	q=dim/(3*lista.size());
	int limite = (3*lista.size());
	
	for (int y=0; y < limite; ++y){
		g2d::set_color({lista[j],lista[j],lista[j]});
		
		for (int x=0; x < y+1; ++x){
			
			
			g2d::fill_rect({x*q,y*q,q,q});
			g2d::fill_rect({y*q,x*q,q,q});
			
		}
		++j;
		if (j == lista.size()){
			j=0;
		}
		
	}	
}


int main(){
	g2d::init_canvas({500,500});
	g2d::main_loop(tick);
}
