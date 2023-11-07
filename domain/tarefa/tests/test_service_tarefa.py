import pytest
from ..models.model_tarefa import Tarefa
from domain.usuario.models.model_usuario import Usuario
from ..services.services_tarefa import TarefaService

@pytest.fixture
def tarefa_exemplo():
    return Tarefa('pofesso', 'Lavar a louça', 'Hoje')


@pytest.fixture
def usuario_exemplo():
    return Usuario('pofesso', '1234')


class TestClass:
    def test_cria_tarefa(self, usuario_exemplo, tarefa_exemplo):
        saida = TarefaService.cria_tarefa(self, 
            usuario_exemplo,
            'Lavar a louça',
            'Hoje'
        )

        assert tarefa_exemplo == saida

    
    