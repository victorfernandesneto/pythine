from ..models.model_tarefa import Tarefa
from domain.usuario.models.model_usuario import Usuario

usuario = Usuario('pofesso', '1234')



class TarefaService:
    def cria_tarefa(self, usuario, nome_da_tarefa, prazo):
        tarefa = Tarefa(usuario.username, nome_da_tarefa, 'Hoje')
        return tarefa