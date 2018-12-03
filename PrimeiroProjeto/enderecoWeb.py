class EndWeb:      
    def __init__(self, url=None, usuario=None, senha=None):
        self.url = 'https://www.facebook.com/login'
        self.usuario = 'aliem82@msn.com'
        self.senha = 'mikel2151*.'
    
    def getUrl(self):
        return self.url

    def getUsuario(self):
        return self.usuario

    def getSenha(self):
        return self.senha
