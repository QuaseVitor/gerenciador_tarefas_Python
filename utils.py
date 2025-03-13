from dataclasses import dataclass

horario = [
           "Manha",
           "Tarde",
           "Noite"           
        ]

caminho_padrao = "./anotacoes.txt"



@dataclass
class tarefa:
    nome: str
    periodo: int
    descricao: str

    def adicionar_tarefa(self):
        while True:    
            
            indisponivel = False
            
            self.nome = input("Nome da tarefa ")
            
            with open(caminho_padrao, "r", encoding="UTF-8") as arquivo:
                conteudo = arquivo.read().strip()
                if conteudo: 
                    busca = conteudo.split("\n")                      
                    for b in busca:
                        if self.nome.strip() == b.strip():
                            print("Ja existe uma tarefa com esse nome. Use outro")  
                            indisponivel = True    
                            break
            if not indisponivel:   
                print("nome libre")   
                break

        while True:
            try:
                for h in horario:
                    print(h)
                self.periodo = input("Qual horario dessa tarefa? ").capitalize()
                if self.periodo in horario:
                    break
                else:
                    print("horario invalido")
                    continue
            except ValueError:
                print("Horario invalido")
                continue
        print(f"Adicionando: {self.nome} - {self.periodo}")
        self.descricao = input("Do que se trata essa tarefa? ")
        while True:    
            try:   
                with open(caminho_padrao, "a", encoding="UTF-8" ) as arquivo:
                    arquivo.write(f"{self.nome} - {self.periodo} +   {self.descricao}.\n")
                    print("\n Tarefa adicionada")
                    break
            except:
                with open(caminho_padrao, "w", encoding="UTF-8") as arquivo:
                    arquivo.write(" anotações ")
                    continue
                
                        
def exibir_especificos(item):
    with open(caminho_padrao, "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.read().strip()
        if conteudo:            
            if item == "Manha" or item == "Tarde" or item == "Noite":
            
                with open(caminho_padrao, "r", encoding="UTF-8") as arquivo:
                    busca = arquivo.read().split(".")
                    for b in busca:
                        if item in b:
                            b = b.replace("+", "\n")
                            print(b)

            elif item == "Todos":
                exibir_tudo()
                
            else:
                print("essa opcao e invalida")
                
        else:
            print("Ainda não há notas para exibir. Adicione uma\n")

def exibir_tudo():
    for i in horario:
        exibir_especificos(i)  

def apagar_tarefa():
    print("Qual tarefa deseja apagar?")
    exibir_tudo()
       
    while True:
        print("Insira o nome da tarefa a ser apagada")
        clear = input().capitalize()
        with open(caminho_padrao, "r", encoding="UTF-8") as arquivo:
            linhas = arquivo.readlines()
            novas_linhas = [linha for linha in linhas if clear not in linha]

            if len(novas_linhas) < len(linhas):
                with open(caminho_padrao, "w", encoding="UTF-8") as arquivo:
                    arquivo.writelines(novas_linhas)

                print("\n Item encontrado e removido!")
                break
            
            else:
                print("Por favor, insira um valor válido.")  
