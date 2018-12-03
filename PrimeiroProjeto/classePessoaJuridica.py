from classePessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj


    def setCnpj(self,cnpj):
        self.cnpj = cnpj

    def getCnpj(self):
        return self.cnpj