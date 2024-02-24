#include <iostream>
using namespace std;

bool char_in_string(string d, string e){
	string f;
	for (int i = 0; i <= d.length(); ++i){
        f = d[i];
		if (f == e){
			return true;
		}
	}
	return false;
}

string caratteri(string stringa1, string stringa2){
	string str_final, a, b;
	
	for (int i = 0; i <= stringa1.length(); ++i){
        a = stringa1[i];
		for (int z = 0; z <= stringa2.length(); ++z){
			b = stringa2[z];
			if ((a == b) && ( false == char_in_string(str_final, a))){
				str_final += a;
				
			}
		}
	}
	return str_final;
}

int main(){
	string a = "the intersection"; string b = "of two strings";
	string result;
	result = caratteri(a, b);
	cout << result;
}