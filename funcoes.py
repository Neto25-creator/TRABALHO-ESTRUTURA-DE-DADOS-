import os , time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")     #esse consegue limpar a tela no windows e também no mac/linux

def sair():                        
    print("Saindo...")
    time.sleep(0.5)
    limpar_tela()
    
def continuar():
    input("Pressione Enter para continuar...")               
    limpar_tela()

