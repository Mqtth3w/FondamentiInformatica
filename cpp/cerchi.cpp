#include <iostream>
#include "g2d/canvas.hpp"
using namespace std;
  
void cerchi(int n) {
    int  centro, raggio, color;
	centro = 300;
	raggio = 300;
	color = 255;
	
	for (int i = 0; i < n; ++i){
		g2d::set_color({color,0,0});
		g2d::fill_circle({centro, centro},raggio);
		raggio -= centro/n;
		color -= 255/(n-1);
	}

}

int main(){
	int n;
	cout << "Numero di cerchi da disegnare?\n";
	cin >> n;
	g2d::init_canvas({600, 600});
	cerchi(n);
	g2d::main_loop();
}