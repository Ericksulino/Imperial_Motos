class Pessoa ():

    __slots__ = ['_nome','_endereco','_cpf','_data_nascimento','_senha']
    def __init__(self, nome,endereco, cpf, data_nascimento,senha):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nm):
        self._nome = nm
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self,end):
        self._endereco = end

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def senha(self):
        return self._senha

    def imprimir_pessoa(self):
        print(self._nome, ", CPF: ", self._cpf,"Endereço: ",self._endereco,",Data de nascimento: ",self._data_nascimento)

class Vendedor(Pessoa):
    
    def __init__(self, nome,endereco,cpf, data_nascimento):
        super().__init__(nome,endereco,cpf, data_nascimento)
        #self._salario = salario
        self._num_vendas = 0

    @property
    def num_vendas(self):
        return self._num_vendas
    
    @num_vendas.setter
    def num_vendas(self,nv):
        self._num_vendas = nv

    def imprimir_vendedor(self):
        super().imprimir_pessoa()
        #print(self._salario)
        print(self._num_vendas)


class Cliente(Pessoa):

    def __init__(self, nome,endereco,cpf, data_nascimento):
        super().__init__(nome,endereco,cpf, data_nascimento)
        #self._profissao = profissao
        #self._renda = renda

    def imprimir_cliente(self):
        super().imprimir_pessoa()
        #print(self._profissao, self._renda)