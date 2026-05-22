# Lista 6 - Orientação a Objetos em Python

Nesta atividade, vocês irão revisitar os principais conceitos de Orientação a Objetos em Python por meio da construção de um pequeno sistema de agenda telefônica. O objetivo é reforçar herança,encapsulamento, propriedades, atributos de classe e métodos estáticos.

Vocês devem criar quatro classes, cada uma em seu módulo:

1. **Contato**

    Use `__slots__` para definir os atributos privados `_nome` , `_telefone` , `_datanasc` (um objeto `datetime.date`) `e _email` . Implemente properties com getters e setters para cada um desses campos, garantindo encapsulamento. Sobrescreva o método `__str__` para que ele retorne, em linhas separadas, o nome, o telefone, a data de nascimento formatada como dd/mm/aaaa e o e-mail.

2. **ContatoEmergencia** (herda de `Contato` )
    
    Além dos atributos herdados, adicione um atributo privado `_prioridade` (booleano, padrão `True`) e exponha-o por meio de uma property somente de leitura.

3. **Evento**

    Cada instância deve armazenar `_descricao` , `_data_inicio` , `_data_fim` (ambos `datetime.date`) e um objeto `Contato` associado. Use um atributo de classe privado `_total_eventos` que é incrementado a cada nova criação de `Evento`. Implemente o método de instância `get_informacoes() → str` (retornando escrição, datas e nome do contato) e o *static method* `get_total_eventos() → int`.

4. **Agenda**

    Mantenha, como atributos de classe privados, listas para contatos e eventos.O construtor opcionalmente pode receber um `Contato` ou um `Evento` para inicialização. Forneça métodos estáticos `contatos() → list[Contato]` e `eventos() → list[Evento]`.

No arquivo **main.py**, monte um menu interativo usando `match/case` com as seguintes opções:

- Criar, editar e listar contatos
- Criar contatos de emergência
- Criar e listar eventos
- Sair (ao sair, exiba o total de eventos via `Evento.get_total_eventos()`)

Use `f-strings` para exibir informações, converta datas com datetime.date e trate erros de entrada. Estruture seu código em cinco arquivos: `contato.py`, `contato_emergencia.py`, `evento.py`, `agenda.py` e `main.py`. Ao final, seu sistema deverá permitir cadastrar e gerenciar contatos, contatos de emergência e eventos, demonstrando claramente o uso dos conceitos de OOP estudados.