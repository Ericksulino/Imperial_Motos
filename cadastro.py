class Cadastro:
    __slots__= ['_lista_pess']
    def __init__(self):
        self._lista_pess = []
    
    def busca(self,cpf):
        for pess in self._lista_pess:
            if pess.cpf == cpf:
                return pess
            else: 
                return None

    def cadastra(self,pessoa):
        exist = self.busca(pessoa.cpf)
        if exist == None:
            self._lista_pess.append(pessoa)
            return True
        else:
            return False
    def impriLis(self):
        print("Pessoas cadastradas:")
        for pess in self._lista_pess:
            pess.imprimir_pessoa()