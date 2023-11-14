from ..models.model_tarefa import Tarefa
from domain.usuario.models.model_usuario import Usuario


usuario = Usuario('pofesso@email.com', '1234')
tarefa = ('pofesso@email.com', 'Lavar a louça', 'Hoje')


class TarefaService:
    @staticmethod
    def cria_tarefa(usuario, nome_da_tarefa, prazo):
        tarefa = Tarefa(usuario.email, nome_da_tarefa, prazo)
        usuario.lista_de_tarefas.append(tarefa)
        return tarefa
    

    @staticmethod
    def deleta_tarefa(usuario, tarefa):
        if tarefa in usuario.lista_de_tarefas:
            usuario.lista_de_tarefas.remove(tarefa)
        else:
            raise ValueError('Tarefa inexistente!')
        

    @staticmethod
    def edita_tarefa(tarefa, nome_novo, prazo_novo):
        tarefa.nome_da_tarefa = nome_novo
        tarefa.prazo = prazo_novo
        return tarefa
    

    @staticmethod
    def marca_completa(tarefa):
        if tarefa.completa:
            tarefa.completa = False
            return tarefa
        tarefa.completa = True
        return tarefa
    

    @staticmethod
    def lista_tarefas(usuario):
        return [f'{tarefa.nome_da_tarefa}, {tarefa.prazo}' for tarefa in usuario.lista_de_tarefas]