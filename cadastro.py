import os;

restaurantes = [{"nome": "Pizzaria do Zé", "categoria": "Italiana", "ativo":False },
                {"nome": "Sushi Place", "categoria": "Japonesa", "ativo":True},
                {"nome": "Burger House", "categoria": "Fast Food", "ativo":False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input("\n Digite uma tecla para voltar ao menu principal")   
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados = {"nome": nome_do_restaurante, "categoria" : categoria, "ativo" : False}
    restaurantes.append(dados)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes")
    linha = "*" * 60
    print(linha)
    print(f"""{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status""")
    print(linha)
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alternar estado do restaurante")
    restaurante_escolhido = input("Digite o nome do restaurante que quer alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante_escolhido == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {restaurante_escolhido} foi ativado com sucesso" if restaurante ["ativo"] else f"O restaurante {restaurante_escolhido} foi destivado com sucesso"
            print (mensagem)

    if not restaurante_encontrado:
        print("Restaurante não encontrado!. Veja se digitou corretamente")

    voltar_ao_menu_principal()    

def finalizar_programa():
    exibir_subtitulo("Programa finalizado")
 
def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def escolher_opcao():

    try:   
        opcao_escolhida = int(input("Escolha uma opção: "))
    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
        
    except: opcao_invalida()   

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__":
    main()
    
    
