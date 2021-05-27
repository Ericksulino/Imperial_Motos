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
    
    def cadas_vend(self,pessoa):
        if self.busca_vend(pessoa.cpf)==None:
            self._lista_vende[pessoa.cpf] = pessoa
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
        if self._lista_motos != {}:
            print("Todas as motos:")
            for key in self._lista_motos:
                print(self._lista_motos[key].imprimeMoto())
        else:
            print("Nenhuma moto cadastrada!")

    def impri_vende(self):
        if self._lista_vende != {}:
            print("Vendedores cadastrados:")
            for key in self._lista_vende:
                self._lista_vende[key].imprimir_pessoa()
        else:
            print("Nenhum vendedor cadastrado!")


'''
Efetuar login,
Cadastrar o vendedor, 
Cadastrar cliente, 
Cadastrar produto, 
Remover cliente, 
Remover vendedor, 
Remover produto, 
Consultar um vendedor, 
Consultar um vendedor, 
Alterar um produto, 
Alterar cliente, 
Alterar vendedor, 
Confirmar Pagamento
'''