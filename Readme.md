# Gerenciador de Tarefas

Este é um simples gerenciador de tarefas em Python, onde o usuário pode adicionar, visualizar, listar e excluir tarefas anotadas. Ele armazena as tarefas em um arquivo de texto, permitindo que o usuário leia ou adicione novas tarefas sempre que necessário.

## Funcionalidades

- **Adicionar Tarefa**: Permite ao usuário inserir o nome, horário e descrição da tarefa. O sistema verifica se já existe uma tarefa com o mesmo nome antes de adicioná-la. As informações são armazenadas no arquivo `anotacoes.txt`.
- **Ler Tarefas Anotadas**: Exibe as tarefas salvas no arquivo, permitindo filtrar por horário, para que o usuário visualize apenas as tarefas desejadas.
- **Apagar Tarefa**: O usuário pode excluir uma tarefa previamente salva no arquivo.
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
   python App.py
   ```

4. Após iniciar o programa, você verá um menu de opções:

   ```
   O que deseja fazer?
   1. Adicionar Tarefa
   2. Ler Tarefas Anotadas
   3. Apagar Tarefa
   4. Sair
   ```

   Escolha uma das opções digitando o número correspondente. O programa irá:

   - Adicionar tarefas ao arquivo `anotacoes.txt`, garantindo que não haja nomes duplicados.
   - Exibir as tarefas já adicionadas, com a opção de filtrar por horário.
   - Permitir excluir uma tarefa previamente anotada.
   - Encerrar o programa.

5. As tarefas serão armazenadas no arquivo `anotacoes.txt` e poderão ser visualizadas posteriormente.

## Estrutura de Arquivos

- **anotacoes.txt**: Arquivo onde as tarefas são armazenadas.
- **app.py**: Arquivo principal que contém a lógica de interação com o usuário e as funções de gerenciamento.
- **utils.py**: Contém as classes e funções auxiliares usadas no programa.

## Exemplo de Uso

### Adicionando uma tarefa:

```
Nome da tarefa: Estudar Python
Qual horário dessa tarefa? Manhã
Do que se trata essa tarefa? Estudar tópicos de programação em Python
```

Se já existir uma tarefa com o mesmo nome, o programa exibirá um aviso e solicitará um nome diferente.

### Lendo tarefas anotadas:

```
Deseja filtrar por horário? (Sim/Não): Sim
Digite o horário desejado: Manhã
```

O programa mostrará apenas as tarefas que correspondem ao horário especificado.

### Apagando uma tarefa:

```
Digite o nome da tarefa que deseja apagar: Estudar Python
Tarefa removida com sucesso!
```

Se o nome da tarefa não for encontrado, o programa avisará ao usuário.

## Contribuições

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork do repositório, criar suas alterações e enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

