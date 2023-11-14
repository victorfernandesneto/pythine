from ..models.model_usuario import Usuario


class UsuarioService:
    @staticmethod
    def cadastra_usuario(email, senha):
        usuario = Usuario(email, senha)
        return usuario
    
    
    @staticmethod
    def atualiza_usuario(usuario, email_novo, senha_nova):
        usuario.email = email_novo
        usuario.senha = senha_nova
        return usuario