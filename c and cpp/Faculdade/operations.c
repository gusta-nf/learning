// Durante a aula ao vivo meu professor passou o exercício para realizarmos contas com duas variáveis, essa foi minha solução.
#include <stdio.h>
int main()
{
    int a;
    int b;
    printf("Digite um primeiro número inteiro: ");
    scanf("%d", &a);
    printf("Digite um segundo número inteiro: ");
    scanf("%d", &b);
    int c = a + b;
    int d = a * b;
    int e = a - b;
    int f = a / b;
    int g = a % b;
    printf("A soma dos seus números é %d, a multiplicação é %d, a subtração é %d e a divisão é %d com resto %d", c, d, e, f, g);
    return 0;
}