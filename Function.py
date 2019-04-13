import Conexao
import Bibliotecas


def Create(id,nome_user, idade_user, email_user, senha_user):
    result =Bibliotecas.hashlib.md5(senha_user.encode())
    senha_nov = (result.hexdigest())
    sql_query =("INSERT INTO users VALUE(DEFAULT,\'{}\',\'{}\',\'{}\',\'{}\')".format(nome_user,
                                                                                      idade_user,
                                                                                      email_user,
                                                                                      senha_nov))
    try:
        if (Conexao.cursor.execute(sql_query)):

            input("\nUsuário cadastrado com sucesso!\n")
            MenuPrincipal(id)
        else:
            print("\nUsuário não cadastrado!\n")
            input()
            MenuPrincipal(id)
    except:
        print(Conexao.cursor.Error)
        Bibliotecas.os.system('pause')

def Read():
    Bibliotecas.os.system('cls')
    sql_query =("SELECT * FROM users;")

    try:
         if (Conexao.cursor.execute(sql_query)):

             data = Conexao.cursor.fetchall()
             for row in data:
                 users_id =row[0]
                 users_nome =row[1]
                 users_idade =row[2]
                 users_email =row[3]
                 users_senha =row[4]
                 print("\n\tInformações do Usuário: {}\n\nNome:\t{}\nIdade:\t{}\nEmail:\t{}\nSenha:\t{}\n".format(users_id,
                                                                                                                  users_nome,
                                                                                                                  users_idade,
                                                                                                                  users_email,
                                                                                                                  users_senha))
             input("Pressione qualquer tecla para continuar...")
             MenuPrincipal(id)
         else:
             print("\nError\n")
             input()

    except:
        print(Conexao.cursor.Error)
        Bibliotecas.os.system('pause')

def ReadEspecifico(id,id_especifico):
    Bibliotecas.os.system('cls')
    sql_query = ("SELECT * FROM users WHERE users_id=\'{}\';".format(id_especifico))

    try:
        if (Conexao.cursor.execute(sql_query)):

            data = Conexao.cursor.fetchall()
            for row in data:
                users_id = row[0]
                users_nome = row[1]
                users_idade = row[2]
                users_email = row[3]
                users_senha = row[4]
                print(
                    "\n\tInformações do Usuário: {}\n\nNome:\t{}\nIdade:\t{}\nEmail:\t{}\nSenha:\t{}\n".format(users_id,
                                                                                                               users_nome,
                                                                                                               users_idade,
                                                                                                               users_email,
                                                                                                               users_senha))
            input("Pressione qualquer tecla para continuar...")
            MenuPrincipal(id)
        else:
            print("\nUsuário inexistente no banco de dados!\n")
            input()
            MenuPrincipal(id)

    except:
        print(Conexao.cursor.Error)
        Bibliotecas.os.system('pause')

def Update(nome,id):
    sql_query = ("UPDATE users SET users_nome=%s WHERE users_id=%s " % (nome,id))

def Delete(id):
    sql_query =("DELETE FROM users WHERE users_id =%d" % (id))


def Login(email,senha):
    result =Bibliotecas.hashlib.md5(senha.encode())
    senha_nov = (result.hexdigest())
    sql_query =("SELECT * FROM users WHERE users_email=\'{}\' AND users_senha=\'{}\';".format(email,senha_nov))

    try:
        if (Conexao.cursor.execute(sql_query)):

            data =Conexao.cursor.fetchall()
            for row in data:
                id=row[0]

            MenuPrincipal(id)
        else:
            print("\nUsuário e/ou Senha inválido(s)\n")
            input()
            MenuLogin()
    except:
        print(Conexao.cursor.Error)
        Bibliotecas.os.system('pause')


def MenuPrincipal(id):
    Bibliotecas.os.system('cls')
    print("\n\tMenu Principal\n")
    print("[1] - Cadastrar um cliente")
    print("[2] - Menu visualizar dados")
    print("[3] - Atualizar seus dados")
    print("[4] - Deletar cliente")
    print("[5] - Sair do programa")
    opcaoMenuPrincipal =int(input("\nDigite um numero:\t"))

    if opcaoMenuPrincipal == 1:
        MenuCadastro(id)
    elif opcaoMenuPrincipal == 2:
        MenuRead(id)
    elif opcaoMenuPrincipal == 3:
        Update()
    elif opcaoMenuPrincipal == 4:
        Delete()
    elif opcaoMenuPrincipal == 5:
        Conexao.conn.close()
    else:
        print("\nDigite uma opção dentre as listadas acima!\n")
        input()
        MenuPrincipal(id)

def MenuCadastro(id):
    Bibliotecas.os.system('cls')
    print("\n\tMenu Principal - Cadastro Cliente\n")
    nome_user = input("Digite seu nome:\t")
    idade_user = int(input("\nDigite sua idade:\t"))
    email_user = input("\nDigite seu e-mail:\t")
    senha_user = input("\nDigite sua senha:\t")
    Create(id,nome_user, idade_user, email_user, senha_user)

def MenuRead(id):
    Bibliotecas.os.system('cls')
    print("\n\tMenu Principal - Visualizar Dados\n")
    print("[1] - Visualizar um cadastro específico")
    print("[2] - Visualizar todos os cadastros")
    print("[3] - Voltar")
    opcaoMenuPrincipal =int(input("\nDigite um numero:\t"))

    if opcaoMenuPrincipal == 1:
        Bibliotecas.os.system('cls')
        id_especifico =input("Digite o id do usuário:\t")
        ReadEspecifico(id,id_especifico)
    elif opcaoMenuPrincipal == 2:
        Read()
    elif opcaoMenuPrincipal == 3:
        MenuPrincipal(id)
    else:
        print("\nDigite uma opção dentre as listadas acima!\n")
        input()
        MenuRead(id)

def MenuLogin():
    Bibliotecas.os.system('cls')
    print("\n\tLogin\n")
    email_user =input("Digite seu e-mail cadastrado:\t")
    senha_user =input("\nDigite sua senha cadastrada:\t")

    Login(email_user,senha_user)