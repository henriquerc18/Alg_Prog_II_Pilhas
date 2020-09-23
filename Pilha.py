from No import No

class Pilha: 

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho 
    
    def adicionarInicio(self, valor ):
        no = No( valor )
        if self.tamanho == 0:
            self.inicio = no    
            self.fim = no    
        else:
            aux = self.inicio
            no.proximo = aux
            aux.anterior = no
            self.inicio = no
        self.tamanho = self.tamanho + 1

    def adicionarFim(self, valor ):
        no = No( valor )
        if self.tamanho == 0:
            self.inicio = no    
            self.fim = no    
        else:
            aux = self.fim
            no.anterior = aux
            aux.proximo = no
            self.fim = no
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")

        texto = ""
        aux = self.inicio
        while( aux ):
            texto += " -> " + aux.dado 
            aux = aux.proximo

        print(texto)
        print( "Tamanho da Lista: " + str(self.tamanho ))


    def imprimirReverso(self):
        if self.inicio == None:
            print("Lista Vazia")
        aux = self.fim
        texto = ""
        while( aux ):
            texto += aux.dado + " <- "
            aux = aux.anterior

        print(texto)    
        print( "Tamanho da Lista: " + str(self.tamanho ))
        

    def excluirInicio( self):
        if self.tamanho == 0 :
            print( "A lista está vazia")
        elif self.tamanho == 1 :
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.tamanho -= 1

    def excluirFim( self):
        if self.tamanho == 0 :
            print( "A lista está vazia")
        elif self.tamanho == 1 :
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -= 1
