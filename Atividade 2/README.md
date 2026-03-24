# Lista 2 - Estruturas de Controle

Resolva os exercícios com a linguagem Python, tente seguir o caminho mais **pythônico** possível.

1. Verifique se uma string é um **palíndromo**, ignorando espaços, pontuações e diferenças entre
maiúsculas e minúsculas.

2. Semáforo inteligente (if/elif/else)

    Leia 3 entradas:
    - `hora` (0–23)
    - `chuva` ( `0` ou 1 )
    - `fluxo` ( `0` baixo, `1` médio, `2` alto)

    Regras:
    - Se `hora` em [7–9] ou [17–19], o tempo base é 60s; senão 35s.
    - Se `chuva==1` , aumente 20%.
    - Se `fluxo==2` , aumente +15s; se `fluxo==0` , diminua −10s.

    Imprima o tempo final (inteiro, arredondando para cima).

3. Crie um programa que verifique se duas palavras ou frases são **anagramas**, ou seja, se possuem os mesmos caracteres (ignorando espaços e maiúsculas/minúsculas).

4. Crie um programa que leia uma lista de palavras e um termo a ser buscado. Utilize um laço `for` para realizar uma busca linear na lista. Se a palavra for encontrada, imprima o índice em que ela está; caso contrário, informe que a palavra não foi encontrada.

5. Leia `a`, `b`, `p` (inteiros).
    Imprima os números de `a` até `b` **incluindo b se encaixar**, usando `range`.

    Regras:
    - se p == 0 → erro.
    - se a < b então p deve ser positivo;
     - se a > b então p deve ser negativo;
     - se não, erro.

    imprima também **quantos valores** foram impressos.

6. Você está simulando um atendimento. Comandos:

- `A` → abrir atendimento (vira estado “aberto”)
- `T` → triagem (só se aberto)
- `E` → encaminhar (só se triado)
- `F` → finalizar (só se encaminhado)
- `S` → sair

    Use `match` para tratar comando e um `while` para repetir até `S`.

    Imprima mensagens de erro quando a transição for inválida (ex.: tentar finalizar sem encaminhar).

7. Leia `n` (inteiro).

- Se n < 0 → erro.
- Calcule `n!` com `for` .
- **Interrompa** se o resultado ultrapassar `1_000_000` e imprima:

    - “passou do limite em k!” (onde k é o momento que estourou)
    - o valor acumulado até estourar
8. Leia `n` (inteiro > 0).

    Some os divisores próprios de n (de 1 até n-1).

    Classifique:
    - soma == n → **perfeito**
    - soma > n → **abundante**
    - soma < n → **deficiente**

    Imprima soma e classificação.
