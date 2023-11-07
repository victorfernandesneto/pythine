import pytest
from ..models.model_tarefa import Tarefa

@pytest.fixture
def tarefa_exemplo():
    return Tarefa('pofesso', 'Lavar a louça', 'Hoje')


class TestClass:
    def test_eq(self, tarefa_exemplo):
        saida = Tarefa('pofesso', 'Lavar a louça', 'Hoje')

        assert tarefa_exemplo == saida


    def test_repr(self, tarefa_exemplo):
        saida = 'Tarefa Lavar a louça do usuário pofesso'

        assert repr(tarefa_exemplo) == saida


 
    def test_atualiza_nome_da_tarefa(self, tarefa_exemplo):
        saida = Tarefa('pofesso', 'Comer cu de curioso', 'Hoje')

        tarefa_exemplo.nome_da_tarefa = 'Comer cu de curioso'

        assert tarefa_exemplo.nome_da_tarefa == saida.nome_da_tarefa

    
    def test_atualiza_prazo(self, tarefa_exemplo):
        saida = Tarefa('pofesso', 'Comer cu de curioso', 'Amanhã')

        tarefa_exemplo.prazo = 'Amanhã'

        assert tarefa_exemplo.prazo == saida.prazo

    
    def test_atualiza_status(self, tarefa_exemplo):
        tarefa_exemplo.completa = True

        assert tarefa_exemplo.completa