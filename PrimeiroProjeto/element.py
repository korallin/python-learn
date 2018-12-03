class Elements:
    def __int__(self, id, nome):
        self.id = id
        self.nome = nome

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
