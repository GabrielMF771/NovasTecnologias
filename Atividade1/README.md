# Lista 1 - Variáveis e Tipos Embutidos
Resolva os exercícios com a linguagem Python, tente seguir o caminho mais pythônico possível.

1. Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*).

2. Peça ao usuário um número como string e uma base (8, 10 ou 16). Converta para inteiro e imprima:valor em decimal valor em hexadecimal ( ```hex()``` )
valor em octal ( ```oct()``` )

3. Sem usar parênteses extras, escreva expressões que resultem em:
- 7
- 13
- 3.5

    usando toda e apenas ```+ - * / // % **``` . Depois, reescreva usando parênteses para deixar a intenção clara.

4. Leia uma frase e gere:
- quantidade de caracteres ( ```len``` )
- primeira e última letra
- frase invertida com fatiamento ```[::-1]```

5. Entrada: uma string no formato ```YYYY-MM-DD HH:MM:SS``` - mensagem

    Exemplo: ```2026-03-12 09:15:07``` - login ok
Extraia com slicing:
- data
- hora
- mensagem

    sem usar ```split()``` (para treinar índice/fatia).

6. Faça uma cifra tipo César:
- a. entrada: texto e deslocamento ( ```int``` )
- b. saída: texto cifrado deslocando letras (apenas A-Z/a-z), mantendo espaços

    Dica: ```ord()``` e ```chr()``` (**builtins**).

7. Crie um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) aparecem na frase. Considere que a contagem deve ser case-insensitive (ou seja, não diferencie maiúsculas de minúsculas).

8. Uma empresa que quer enviar dados pela internet pediu-lhe que escrevesse um programa que criptografe dados a fim de que eles possam ser transmitidos com maior segurança. Todos os dados são transmitidos como inteiros de quatro dígitos. Seu aplicativo deve ler um inteiro de quatro dígitos inserido pelo usuário e criptografá-lo da seguinte maneira: substitua cada dígito
pelo resultado da adição de 7 ao dígito, obtendo o restante depois da divisão do novo valor por 10. Troque então o primeiro dígito pelo terceiro e o segundo dígito pelo quarto. Então, imprima o inteiro criptografado. Escreva um aplicativo separado que receba a entrada de um inteiro de quatro dígitos criptografado e o descriptografe (revertendo o esquema de criptografia) para
formar o número original.
