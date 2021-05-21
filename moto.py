class Moto ():
    __slots__ = ['_num_chas','_nome','_marca','_tipo','_ano','_valor']
    def __init__(self,num_chas,nome,marca,tipo,ano,valor):
        self._num_chas = num_chas
        self._nome = nome
        self._marca = marca
        self._tipo = tipo
        self._ano = ano
        self._valor = valor
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nm):
        self._nome = nm
    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,mar):
        self._marca = mar
    
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self,an):
        self._ano = an

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self,tip):
        self._tipo = tip
    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self,val):
        self._valor = val
    
    @property
    def num_chas(self):
        return self._num_chas

    def imprimeMoto(self):
        return ' Nome: {} \n Marca: {} \n Tipo: {} \n Ano: {} \n'.format(self._nome,self.marca,self._tipo,self._ano,self._valor)
