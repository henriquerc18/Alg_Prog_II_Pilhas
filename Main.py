from Pilha import Pilha

pilha = Pilha()
op = "" 

while(op != "0" ):
    print("\n----------------------")
    print("0 - Fim")
    print("1 - Inserir")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Mostrar Tamanho")
    
    op = input("Digite sua opção: ")

    if op == "0':
        break
    
    if op == "1":
        item = input("Informe um valor: ")
        pilha.inserirItem(item)

    if op == "2":
        item = input("Informe um valor: ")
        pilha.excluirItem(item)

    if opcao == "3":
        lista.listarDados()

    if opcao == "4":
        lista.mostrarTamanho()
print("Fim")
 
