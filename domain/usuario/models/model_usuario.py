class Usuario:
    def __init__(self, username, senha):
        self._username = username
        self._senha    = senha
        self._lista_de_tarefas = []


    @property
    def username(self):
        return self._username
    
    
    @property
    def senha(self):
        return self._senha
    

    @property
    def lista_de_tarefas(self):
        return self._lista_de_tarefas
    

    @username.setter
    def username(self, username_novo):
        self._username = username_novo
        

    @senha.setter
    def senha(self, senha_nova):
        self._senha = senha_nova

    
    def __eq__(self, outro):
        return self._username == outro._username


    def __repr__(self):
        return f'Usuário {self._username}'
