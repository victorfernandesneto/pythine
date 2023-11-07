from ..models.model_usuario import Usuario

class UsuarioService:
    def cadastra_usuario(self, username, senha):
        usuario = Usuario(username, senha)
        return usuario
    
    def atualiza_usuario(self, usuario, username_novo, senha_nova):
        usuario.username = username_novo
        usuario.senha = senha_nova
        return usuario