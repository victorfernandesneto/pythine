from ..models.model_tarefa import Tarefa
from domain.usuario.models.model_usuario import Usuario


usuario = Usuario('pofesso', '1234')
tarefa = ('pofesso', 'Lavar a louça', 'Hoje')


class TarefaService:
    def cria_tarefa(self, usuario, nome_da_tarefa, prazo):
        tarefa = Tarefa(usuario.username, nome_da_tarefa, 'Hoje')
        usuario.lista_de_tarefas.append(tarefa)
        return tarefa
    

    def deleta_tarefa(self, usuario, tarefa):
        if tarefa in usuario.lista_de_tarefas:
            usuario.lista_de_tarefas.remove(tarefa)
        else:
            raise ValueError('Tarefa inexistente!')