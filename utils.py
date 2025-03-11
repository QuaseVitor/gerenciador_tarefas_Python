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
        self.nome = input("Nome da tarefa ")
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
        self.descricao = input("Do que se trata essa tarefa? ")
        while True:    
            try:   
                with open(caminho_padrao, "a", encoding="UTF-8" ) as arquivo:
                    arquivo.write(f"{self.nome} - {self.periodo}+   {self.descricao}\n")
                    break
            except:
                with open(caminho_padrao, "w", encoding="UTF-8") as arquivo:
                    arquivo.write(" anotações ")
                    continue
                
    
    def exibir_tarefa(self):
        print(f"{self.nome}\n {self.periodo}\n {self.descricao}")
        
def exibir_dados_armazenados():
    with open(caminho_padrao, "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.read().strip()
        if conteudo: 
            linhas = conteudo.split("\n")
            for linha in linhas:
                linha_formatada = linha.replace("+", "\n")  # Substitui "+" por quebra de linha
                print( "\n" + linha_formatada)  # Exibe a linha e adiciona um parágrafo extra
        else:
            print("Ainda não há notas para exibir. Adicione uma\n")