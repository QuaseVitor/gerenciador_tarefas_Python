from utils import *

Tarefa = tarefa(nome = ' ', descricao = ' ', periodo = ' ')

while True:
    try:
        print("\no que deseja fazer?\nAdicionar Tarefa \nLer Tarefas anotadas\nSair")
        decisao = input("").capitalize()
    except ValueError:
        print("Opção Invalida")
        continue
    
    if decisao.startswith("Ad"):
        Tarefa.adicionar_tarefa()
        
    elif decisao.startswith("Ler") or decisao.startswith("Anot"):
        exibir_dados_armazenados()
        
    elif decisao == 'Sair':
        print("Fim de exibição")
        break
        
    else: 
        print("Opcao invalida")