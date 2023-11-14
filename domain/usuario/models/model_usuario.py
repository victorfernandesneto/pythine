class Usuario:
    def __init__(self, email, senha):
        self._email = email
        self._senha    = senha
        self._lista_de_tarefas = []


    @property
    def email(self):
        return self._email
    
    
    @property
    def senha(self):
        return self._senha
    

    @property
    def lista_de_tarefas(self):
        return self._lista_de_tarefas
    

    @email.setter
    def email(self, email_novo):
        self._email = email_novo
        

    @senha.setter
    def senha(self, senha_nova):
        self._senha = senha_nova

    
    def __eq__(self, outro):
        return self._email == outro._email


    def __repr__(self):
        return f'Usuário {self._email}'
