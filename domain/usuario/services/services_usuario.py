from ..models.model_usuario import Usuario


class UsuarioService:
    @staticmethod
    def cadastra_usuario(username, senha):
        usuario = Usuario(username, senha)
        return usuario
    
    
    @staticmethod
    def atualiza_usuario(usuario, username_novo, senha_nova):
        usuario.username = username_novo
        usuario.senha = senha_nova
        return usuario