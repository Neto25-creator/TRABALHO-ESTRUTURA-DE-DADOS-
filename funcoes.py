import os , time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")     #limpar tela no windows e mac

def sair():                        
    print("Saindo...")
    time.sleep(1)
    limpar_tela()
    
def continuar():
    input("Pressione Enter para continuar...")               
    limpar_tela()

def parar_operacao():
    input("Operação cancelada. Pressione Enter para continuar...")
    limpar_tela()
