#include <iostream>
#include <string>
using namespace std;

int main()
{
    int opcao;
    do {
        cout<<"\n1 - Cadastro";
        cout<<"\n2 - Registro";
        cout<<"\n0 - Sair\n";
        cin >> opcao;
    } while (opcao != 0);
    
    return 0;
}