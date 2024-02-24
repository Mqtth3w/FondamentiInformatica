#include <iostream>
#include <vector>
using namespace std;

vector<int> reverse(vector<int> interi){
	vector<int> result;
	if (interi.size() <= 1){
		return interi;
	}
	result = reverse({interi.begin()+1 , interi.end()});
	result.push_back(interi[0]);
	return result;
}

int main (){
	vector <int> vettoree = {0,1,2,3,4,5,6,7,8,9};
	vector<int> stampa = reverse(vettoree);
	for (auto n: stampa){
		cout << n << " ";
	}
}