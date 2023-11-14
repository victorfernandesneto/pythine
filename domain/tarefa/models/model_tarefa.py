class Tarefa:
    def __init__(self, email, nome_da_tarefa, prazo):
        self._email = email
        self._nome_da_tarefa = nome_da_tarefa
        self._prazo = prazo
        self._completa = False


    @property
    def nome_da_tarefa(self):
        return self._nome_da_tarefa
    
    
    @property
    def prazo(self):
        return self._prazo
    
    
    @property
    def completa(self):
        return self._completa
    
    
    @nome_da_tarefa.setter
    def nome_da_tarefa(self, novo_nome):
        self._nome_da_tarefa = novo_nome

    
    @prazo.setter
    def prazo(self, novo_prazo):
        self._prazo = novo_prazo

    
    @completa.setter
    def completa(self, novo_status):
        self._completa = novo_status


    def __eq__(self, outro):
        return self._email == outro._email and self._nome_da_tarefa == outro._nome_da_tarefa


    def __repr__(self):
        return f'Tarefa {self._nome_da_tarefa} do usuário {self._email}'