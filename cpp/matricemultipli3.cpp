#include <iostream>
#include <vector>
#include "g2d\basic.hpp"
using namespace std;

int main(){
	int rows, cols, n, numero, multiprow=0, multipcol=0;
	vector <int> matrix;
	
	cout << "righe e colonne della matrice?\n";
	cin >> rows >> cols;
	n = cols*rows;
	
	for (int i = 0; i < n; ++i){
		numero = g2d::randint(0, 99);
		matrix.push_back(numero);
	}
	
	
	for (int z = 0; z < rows; ++z){
		for (int j = 0; j < cols; ++j){
			if ((matrix[z*cols+j] % 3) == 0){
				++multiprow;
			}
			if ((matrix[j*cols+z] % 3) == 0){
				++multipcol;
			}
		}
	
	}
	
	/*
	for (int k = 0; k<matrix.size();++k){
		if (matrix[k] % 3 == 0){
			++multiprow;
		}
	}
	*/
	cout << "Multipli di tre nelle righe: " << multiprow; //<< "\n";
	cout << "\n" << "Multipli di tre nelle colonne: " << multipcol << "\n";
	for (auto n: matrix){
		cout << n << " ";
	}
}