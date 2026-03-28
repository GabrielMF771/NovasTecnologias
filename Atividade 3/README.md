# Lista 3 - Coleções em Python

Resolva os exercícios com a linguagem Python, tente seguir o caminho mais **pythônico** possível.

**1.** Dada uma lista de intervalos representados por tuplas (início, fim), escreva um programa que mescle os intervalos que se sobrepõem. Por exemplo, dado os intervalos ```[(1, 4), (2, 5), (7, 9)]``` , a saída deve ser ```[(1, 5), (7, 9)]``` .

**2.** Dada uma lista de números, conte a frequência de cada número e, em seguida, filtre e exiba somente os números que aparecem um número mínimo de vezes (por exemplo, pelo menos 3 vezes).

**3.** Dada uma lista de números inteiros e um valor alvo, determine se existe um subconjunto cuja soma seja exatamente igual ao valor alvo.

**4.** Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.

Exemplo: ```(())``` **OK** ```()()(()())``` **OK** ```( ) )``` **Erro**

Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.

**5.** Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:

- os valores comuns às duas listas
- os valores que só existem na primeira
- os valores que existem apenas na segunda
- uma lista com os elementos não repetidos das duas listas.
- a primeira lista sem os elementos repetidos na segunda

**6.** Um número primo é qualquer número inteiro maior que 1, que é uniformemente divisível apenas por ele mesmo e por 1. O **Crivo de Eratóstenes** é um método para encontrar números primos. Ele opera como segue:

a. Crie um array de inteiro com todos os elementos inicializados como 1. Os elementos do array com índices primos permanecerão 1. Todos os outros elementos do array por fim são configurados como 0.

b. Iniciando com o índice de array 2, determine se um dado elemento é 1. Se for, faça um loop pelo restante do array e configure como 0 cada elemento cujo índice é um múltiplo do índice para o elemento com valor 1. Então, continue o processo com o próximo elemento com valor 1. Para o índice de array 2, todos os elementos além do elemento 2 no array que tiverem índices que são múltiplos de 2 (índices 4, 6, 8, 10 etc.) serão configurados como 1; para o índice de array 3, todos os elementos além do elemento 3 no array que tiverem índices que são múltiplos de 3 (índices 6, 9, 12, 15 etc.) serão configurados como 0; e assimpor diante. 
    
Quando esse processo for concluído, os elementos de array que ainda forem 1 indicam que o índice é um número primo. Esses índices podem ser exibidos. Escreva um aplicativo que utiliza um array de 1.000 elementos para determinar e exibir os números primos entre 2 e 999. Ignore elementos de array 0 e 1.