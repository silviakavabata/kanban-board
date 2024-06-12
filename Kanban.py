## Cadastro de usuário ##
# Pede Usuário
# Pede Senha
# Salva em um dicionário
# > Futuras implementações: tratar usuarios e senhas | Deixar redefinir senha

cadastros_usuarios = {}

def cadastrar_usuario(cadastros_usuarios):
    usuario = input("Digite um nome de usuário: ")
    #Verifica se usuário já está cadastrado
    if usuario in cadastros_usuarios:
        print("Usuário já cadastrando. Encaminhando para login.")
        login(cadastros_usuarios)
        return #Chamar o login
    
    senha = input("Digite uma senha: ")
    #Adiciona usuário e senha no dicionário de cadastros
    cadastros_usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")
    return


## Login ##
# Verifica se usuário e senha estão no dicionário de cadastro
# Se não, fica pedindo
# > Futuras implementações: permitir usuário voltar pro menu principal

def login(cadastros_usuarios):
    while True:
        #Pede usuário e verifica se está cadastrado
        usuario_input = input("Usuário: ")
        if usuario_input not in cadastros_usuarios:
            print("Usuário " + usuario_input + " não encontrado. Tente novamente.")
            continue
        #Pede senha e verifica se está correta
        senha_input = input("Senha: ")
        if cadastros_usuarios[usuario_input] != senha_input:
            print("Senha incorreta. Tente novamente.")
            continue
        #Se tudo estiver correto, retorna sucesso
        print("Login bem sucedido!")
        return True
    
'''cadastrar_usuario(cadastros_usuarios)
login(cadastros_usuarios)
cadastrar_usuario(cadastros_usuarios)'''


## Mostra listas de tarefas, se não há, retorna que quadro está vazio ##
backlog = []
aFazer = []
emAndamento = []
finalizado = []

def printa_listas(backlog,aFazer,emAndamento,finalizado):
    if not backlog or not aFazer or not emAndamento or not finalizado:
        print("Não há cards cadastrados ainda.")
        return #Mandar para cadastro de Cards
    else:
        print("Backlog: " + backlog + "\n"
            "A Fazer: " + aFazer + "\n"
            "Em Andamento: " + emAndamento + "\n"
            "Finalizado: " + finalizado + "\n")
        return

## Menu de Opções ##
# 1- Cadastrar card -> Pede Nome Card e Descrição -> Cadastra Card com número id
# 2- Mover card -> Pede id Card -> Onde mover "Backlog", "A fazer", "Em andamento", "Finalizado"
# 3- Editar card -> Pede id Card
# 4- Excluir card -> Pede id Card
# 5- Sair -> Fecha sistema