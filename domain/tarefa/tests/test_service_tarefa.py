import pytest
from ..models.model_tarefa import Tarefa
from domain.usuario.models.model_usuario import Usuario
from ..services.services_tarefa import TarefaService


@pytest.fixture
def tarefa_exemplo():
    return Tarefa('pofesso@email.com', 'Lavar a louça', 'Hoje')


@pytest.fixture
def usuario_exemplo():
    return Usuario('pofesso@email.com', '1234')


class TestClass:
    def test_cria_tarefa(self, usuario_exemplo, tarefa_exemplo):
        saida = TarefaService.cria_tarefa( 
            usuario_exemplo,
            'Lavar a louça',
            'Hoje'
        )

        assert tarefa_exemplo == saida

    
    def test_adiciona_tarefa_no_usuario(self, usuario_exemplo, tarefa_exemplo):
        saida = [tarefa_exemplo]

        TarefaService.cria_tarefa(
            usuario_exemplo,
            'Lavar a louça',
            'Hoje'
        )

        assert usuario_exemplo.lista_de_tarefas == saida


    def test_retira_tarefa_do_usuario(self, usuario_exemplo, tarefa_exemplo):
        saida = []

        TarefaService.cria_tarefa( 
            usuario_exemplo,
            'Lavar a louça',
            'Hoje'
        )

        TarefaService.deleta_tarefa(
            usuario_exemplo,
            tarefa_exemplo
        )

        assert usuario_exemplo.lista_de_tarefas == saida

    
    def test_retira_tarefa_inexistente(self, usuario_exemplo, tarefa_exemplo):
        with pytest.raises(ValueError):
            TarefaService.deleta_tarefa(
                usuario_exemplo,
                tarefa_exemplo
            )

    
    def test_muda_nome_e_prazo_da_tarefa(self, tarefa_exemplo):
        saida = Tarefa('pofesso@email.com', 'Comprar ração dos gatos', 'Hoje de manhã')
        
        TarefaService.edita_tarefa(
            tarefa_exemplo,
            'Comprar ração dos gatos',
            'Hoje de manhã'
        )

        assert tarefa_exemplo == saida and tarefa_exemplo.prazo == saida.prazo

    
    def test_marcar_tarefa_completa(self, tarefa_exemplo):
        tarefa_exemplo = TarefaService.marca_completa(tarefa_exemplo)

        assert tarefa_exemplo.completa == True

    
    def test_marca_e_desmarca_tarefa_completa(self, tarefa_exemplo):
        tarefa_exemplo = TarefaService.marca_completa(tarefa_exemplo)
        tarefa_exemplo = TarefaService.marca_completa(tarefa_exemplo)

        assert tarefa_exemplo.completa == False


    def test_devolve_lista_de_tarefas_vazia(self, usuario_exemplo):
        saida = []

        assert TarefaService.lista_tarefas(usuario_exemplo) == saida

    
    def test_devolve_lista_com_tarefas(self, usuario_exemplo, tarefa_exemplo):
        saida = ['Lavar a louça, Hoje']

        TarefaService.cria_tarefa( 
            usuario_exemplo,
            'Lavar a louça',
            'Hoje'
        )

        assert TarefaService.lista_tarefas(usuario_exemplo) == saida