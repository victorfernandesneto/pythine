import pytest
from ..models.model_usuario import Usuario
from ..services.services_usuario import UsuarioService

@pytest.fixture
def usuario_exemplo():
    return Usuario('pofesso', '1234')


class TestClass:
    def test_cria_usuario(self, usuario_exemplo):
        usuario = UsuarioService.cadastra_usuario('pofesso', '1234')

        assert usuario == usuario_exemplo

    def test_atualiza_cadastro(self, usuario_exemplo):
        usuario = Usuario('victao', '1234')

        usuario_exemplo = UsuarioService.atualiza_usuario(usuario_exemplo, 'victao', '1234')

        assert usuario == usuario_exemplo