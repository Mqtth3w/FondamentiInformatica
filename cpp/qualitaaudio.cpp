#include <iostream>

using namespace std;

class Audio_quality{
	double sample_rate; 
	int channels, bits_per_sample;
	
public: 
	Audio_quality(double frequenza, double canali, int bitsrete){
		sample_rate = frequenza; channels = canali; bits_per_sample = bitsrete;
	}
	
	double byte_rate(){
		double result;
		result = (sample_rate*channels*bits_per_sample);
		return result;
	}
	
	double audio_size(double durata){
		double result;
		result = (sample_rate*channels*bits_per_sample*durata);
		return result;
	}
	
};


int main(){
	double frequenza, durata, result;
	int canali, bitsrete;
	
	cout << "Frequenza di campionamento?\n";
	cin >> frequenza;
	cout << "\n" << "Numero di canali?\n";
	cin >> canali;
	cout << "\n" << "Bit per campione?\n";
	cin >> bitsrete;
	
	Audio_quality a = Audio_quality(frequenza, canali, bitsrete);
	
	if ((frequenza < 0)|| (canali < 0) || (bitsrete < 0)){
		cout << "La frequenza, i canali e i bit per campione non possono essere minori di zero\n";
		return 0;
	}
	result = a.byte_rate();
	cout << "Occupazione di un secondo di audio\n" << result << "\n";
	
	cout << "Per l'occupazione su un intervallo di tempo inserire la durata del campionamento in secondi\n";
	cin >> durata;
	while (durata > 0){
		result = a.audio_size(durata);
		cout << "Occupazione: " << result << "\n";
		cout << "Per l'occupazione su un intervallo di tempo inserire la durata del campionamento in secondi\n";
		cin >> durata;
	} 
	cout << "La durata non puo essere minore di zero";
	return 0;
	
}