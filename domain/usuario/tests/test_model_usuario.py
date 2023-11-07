import pytest
from domain.usuario.models.model_usuario import Usuario

@pytest.fixture
def usuario_exemplo():
    return Usuario('pofesso', '1234')


class TestClass:
    def test_eq(self, usuario_exemplo):
        saida = Usuario('pofesso', '1234')

        assert usuario_exemplo == saida


    def test_repr(self, usuario_exemplo):
        saida = 'Usuário pofesso'

        assert repr(usuario_exemplo) == saida


    def test_atualiza_username(self, usuario_exemplo):
        saida = Usuario('victao', '4321')

        usuario_exemplo.username = 'victao'
        
        assert usuario_exemplo.username == saida.username

    
    def test_atualiza_senha(self, usuario_exemplo):
        saida = Usuario('victao', '4321')

        usuario_exemplo.senha = '4321'

        assert usuario_exemplo.senha == saida.senha