from utils import *

Tarefa = tarefa(nome = ' ', descricao = ' ', periodo = ' ')

while True:
    try:
        print("\nO que deseja fazer?\nAdicionar Tarefa \nApagar Tarefa\nExibir Tarefas anotadas\nSair")
        decisao = input("").capitalize()
    except ValueError:
        print("Opção Invalida")
        continue
    
    if decisao.startswith("Ad"):
        Tarefa.adicionar_tarefa()
        
    elif decisao.startswith("Exi") or decisao.startswith("Anot"):
        print("Deseja exibir as anotacoes de qual horario? ")
        for h in horario:
            print(h)
        print("ou todos?")    
        search = input().capitalize()
        
        exibir_especificos(search)    
    
    elif decisao.startswith("Apa"):
        apagar_tarefa()
        
    elif decisao == 'Sair':
        print("Fim de exibição")
        break
        
    else: 
        print("Opcao invalida")