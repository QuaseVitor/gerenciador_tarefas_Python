# Gerenciador de Tarefas

Este é um simples gerenciador de tarefas em Python, onde o usuário pode adicionar, visualizar e listar tarefas anotadas. Ele armazena as tarefas em um arquivo de texto, permitindo que o usuário leia ou adicione novas tarefas sempre que necessário.

## Funcionalidades

- **Adicionar Tarefa**: Permite ao usuário inserir o nome, horário e descrição da tarefa. As informações são armazenadas no arquivo `anotacoes.txt`.
- **Ler Tarefas Anotadas**: Exibe as tarefas salvas no arquivo, formatadas de forma que o horário e a descrição sejam claramente apresentados.
- **Sair**: Finaliza o programa.

## Requisitos

Este projeto foi desenvolvido com Python 3. O código utiliza uma biblioteca interna:

- `dataclasses` (para criação de classes de dados simples)

Não há dependências externas necessárias além do Python.

## Como Usar

1. Clone o repositório ou baixe os arquivos para o seu computador.
   
2. Abra o terminal e navegue até a pasta onde os arquivos estão localizados.

3. Execute o programa com o seguinte comando:

    ```bash
    python nome_do_arquivo.py
    ```

4. Após iniciar o programa, você verá um menu de opções:

    ```
    O que deseja fazer?
    Adicionar Tarefa
    Ler Tarefas Anotadas
    Sair
    ```

    Escolha uma das opções digitando o número correspondente ou o nome completo da ação. O programa irá:
    
    - Adicionar tarefas ao arquivo `anotacoes.txt`.
    - Exibir as tarefas já adicionadas.
    - Permitir que você saia do programa.

5. As tarefas serão armazenadas no arquivo `anotacoes.txt` e poderão ser visualizadas posteriormente.

## Estrutura de Arquivos

- **anotacoes.txt**: Arquivo onde as tarefas são armazenadas.
- **app.py**: Arquivo principal que contém a lógica de interação com o usuário e as funções de gerenciamento.
- **utils.py**: Contém as classes e funções auxiliares usadas no programa.

## Exemplo de Uso

Após executar o programa e escolher a opção "Adicionar Tarefa", você será solicitado a preencher os seguintes campos:

```
Nome da tarefa: Estudar Python
Qual horário dessa tarefa? Manha
Do que se trata essa tarefa? Estudar tópicos de programação em Python
```

Em seguida, a tarefa será salva e poderá ser exibida na opção "Ler Tarefas Anotadas".

## Contribuições

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork do repositório, criar suas alterações e enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
