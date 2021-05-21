class Loja():
    __slots__= ['_lista_clie','_lista_vende','_lista_motos']
    def __init__(self):
        self._lista_clie = {}
        self._lista_vende = {}
        self._lista_motos = {}
    
    def busca_clie(self,cpf):
        return self._lista_clie.get(cpf,None)
       
    def busca_vend(self,cpf):
        return self._lista_vende.get(cpf,None)
        
    def busca_moto(self,numChas):
        return self._lista_motos.get(numChas,None)
        
    def cadas_clie(self,pessoa):
        if self.busca_clie(pessoa.cpf)==None:
            self._lista_clie[pessoa.cpf] = pessoa
            return True
        else:
            return False
    def cadas_clie(self,pessoa):
        if self.busca_vend(pessoa.cpf)==None:
            self._lista_clie[pessoa.cpf] = pessoa
            return True
        else:
            return False

    def cadas_moto(self,moto):
        if self.busca_vend(moto.num_chas)==None:
            self._lista_motos[moto.num_chas] = moto
            return True
        else:
            return False
    
    def venda(self,numChas,cpfCli,cpfVen):
        if self.busca_moto(numChas)!=None:
            if self.busca_vend(cpfVen)!=None:
                if self.busca_clie(cpfCli)!=None:
                    self._lista_vende[cpfVen].num_vendas+=1
                    del self._lista_motos[numChas]
                    return True
        
        return False

    def impri_todas_motos(self):
        print("Todas as motos:")
        for moto in self.lista_motos:
            print(moto.imprimeMoto())

    def impri_vende(self):
        print("Vendedores cadastrados:")
        for pess in self.lista_vende:
            pess.imprimir_pessoa()