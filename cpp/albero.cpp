#include "g2d\canvas.hpp"
#define _USE_MATH_DEFINES
#include <cmath>

using namespace std;


void albero(double x, double y, double tronco, double angolo){
	double x1, y1, t;
    x1 = x + cos(angolo) * tronco;
    y1 = y + sin(angolo) * tronco;
    g2d::draw_line({int(x), int(y)}, {int(x1), int(y1)});
    if (tronco < 5){
        g2d::set_color({0,255,0});
		g2d::draw_line({int(x), int(y)}, {int(x1), int(y1)});
    }
	else{
		t = tronco*4/5;
        g2d::set_color({30,30,0});
        albero(x1, y1, t, angolo+M_PI/6);
		g2d::set_color({30,30,0});
        albero(x1, y1, t, angolo-M_PI/6);
	}
}
        
int main(){
    g2d::init_canvas({1100, 650});
    albero(550, 650, 125, -M_PI/2);
    g2d::main_loop();
}
    