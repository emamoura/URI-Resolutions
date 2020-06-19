#include <iostream>
#include <vector>

using namespace std;

int main() {

    string cidade[8] = {"Brasilia","Salvador","Sao Paulo","Rio de Janeiro","Juiz de Fora","Campinas","Vitoria","Belo Horizonte"};
    int DDD[8] = {61, 71, 11, 21, 32, 19, 27, 31};

    int numero;
    cin >> numero;
    int contador = 0;
    for(int i = 0; i < 8; i++){
        if(numero == DDD[i]){
            cout << cidade[i] << endl;
            contador = 0;
            break;
        }
        contador = 1;
    }
    if(contador == 1){
        cout << "DDD nao cadastrado" << endl;
    }
    

    return 0;
}