#include <iostream>
#include "g2d\canvas.hpp"
using namespace std;
  
void cerchi_casuali(){
    int  centro, raggio, color;
	centro = 300;
	raggio = 200;

	while (raggio > 10){
		g2d::set_color({g2d::randint(0, 255),
						g2d::randint(0, 255),
						g2d::randint(0, 255)});		
		g2d::fill_circle({centro, centro},raggio);
		raggio -= g2d::randint(0, raggio);
	}
}

int main(){
	g2d::init_canvas({600, 600});
	cerchi_casuali();
	g2d::main_loop();
}