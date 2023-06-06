from dataclasses import dataclass

@dataclass
class User: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = password 
        self.is_logged_in = False 

    def login(self, username, password): 
        if username == self.username and password == self.password: 
            self.is_logged_in = True 
            print('Login com sucesso.')
        else: 
            print('Nome de usuário ou senha inválidos.') 

    def logout(self): 
        self.is_logged_in = False 
        print('Desconectado.') 

    def update_password(self, new_password): 
        self.password = new_password 
        print('Senha atualizada.') 


def register() : 
    username = input('Digite um nome de usuário: ') 
    password = input('Digite uma senha: ') 
    user = User(username, password) 
    users.append(user) 
    print('Registro bem-sucedido.') 


def login(): 
    username = input('Digite seu nome de usuário: ') 
    password = input('Digite sua senha: ') 

    for user in users: 
        if user.username == username:
            user.login(username, password) 
            return 

    print('Usuário não encontrado.') 


def logout(): 
    for user in users: 
        if user.is_logged_in: 
            user.logout() 
            return 

    print('Nenhum usuário está conectado no momento.') 


def update_password( ): 
    for user in users: 
        if user.is_logged_in: 
            new_password = input('Digite uma nova senha: ') 
            user.update_password(new_password) 
            return 

    print('Nenhum usuário está conectado no momento.') 

users = [] 

while True: 
    print('\n1 . Cadastre-se') 
    print('2. Login') 
    print('3. Logout')
    print('4. Update Password') 
    print('5. Exit') 

    menu = int(input('Digite sua escolha: ')) 

    if menu == 1: 
        register() 
    elif menu == 2: 
        login() 
    elif menu == 3: 
        logout() 
    elif menu == 4: 
        update_password() 
    elif menu == 5: 
        print('Voce saiu!') 
        break 
    else: 
        print('Inválido menu. Tente novamente.')
