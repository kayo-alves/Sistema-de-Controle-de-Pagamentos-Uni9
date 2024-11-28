/*
Este código em C usa dados dos funcionários inseridos para calcular o valor total do pagamento que será efetuado para o mesmo.
O cálculo é feito com base no seu salário, no valor da sua hora extra baseado no salário, e na possível existência de descontos salariais.
Entende-se que, para esta empresa, todos os funcionários possuem uma carga horária de 8h/dia ou 220h/mês
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
    char pergunta;
    double salario, desconto, pag_total, valor_hora_extra = 0.0;
    double hora_extra, minutos_extra;
    int id_func;
    char nome_func[50];

    // loop do-while para perguntar ao usuário se deseja continuar inserindo novos dados de pagamentos
    do {

        printf("Insira o ID do funcionário: ");
        scanf("%i", &id_func);

        // Limpar o buffer de entrada do scanf anterior
        while (getchar() != '\n');

        printf("Insira o nome do funcionário: ");
        fgets(nome_func, sizeof(nome_func), stdin); // fgets usado para capturar inputs em strings de forma mais prática

        // Remover o '\n' da string capturada, caso esteja presente
        nome_func[strcspn(nome_func, "\n")] = '\0';

        printf("Insira o salário do funcionário: ");
        scanf("%lf", &salario);

        // Limpar o buffer de entrada do scanf anterior
        while (getchar() != '\n');

        printf("Insira a quantidade de horas extras, se nenhuma, insira 0: ");
        scanf("%lf", &hora_extra);

        printf("Insira os minutos extras trabalhados (minutos): ");
        scanf("%lf", &minutos_extra);

        printf("Insira o valor de descontos do funcionário em reais, se não houver insira 0: ");
        scanf("%lf", &desconto);

        // calcula o total de horas extras trabalhadas, com base nas horas e minutos inseridos
        double total_horas_extra = hora_extra + (minutos_extra / 60.0);

        // Cálculo de horas extras em reais, se houver
        if (total_horas_extra > 0)
        {
            valor_hora_extra = total_horas_extra * ((salario / 220.0) * 1.5);
            // O valor da hora é: Total de horas extras * (salário do funcionário / carga horária mensal) * acréscimo de 50%)
            // O acréscimento de 50% existe devido a CLT, que regulariza que os a hora extra trabalhada deve valer 50% a mais do que o valor hora normal.
        }

        // Cálculo do pagamento total
        pag_total = salario + valor_hora_extra - desconto;


        // Loop para uma melhor visualização dos dados coletados
        printf("\n");
        for (int i = 0; i < 30; i++) {
            printf("-");
        }
        printf("\n");

        printf("ID: %i\n", id_func);
        printf("Nome: %s\n", nome_func);
        printf("Salário mensal: R$ %.2lf\n", salario);
        printf("horas extras trabalhadas (em horas): %.1lf\n", total_horas_extra);
        printf("Desconto salarial: R$ %.2lf\n", desconto);
        printf("Pagamento total: R$ %.2lf\n", pag_total);

        // fechamento da visualização dos dados
        for (int i = 0; i < 30; i++) {
            printf("-");
        }
        printf("\n\n");

        // Pergunta ao usuário se eles deseja continuar inserindo dados
        printf("Deseja continuar? \nInsira 'S' para Sim e 'N' para Não: ");

        while (getchar() != '\n'); // Limpar o buffer de entrada do scanf anterior
        scanf(" %c", &pergunta);

    } while (pergunta == 's' || pergunta == 'S');

    return 0;
}
