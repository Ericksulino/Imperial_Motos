class Pessoa ():

    #__slots__ = ['_nome','_endereco','_cpf','_data_nascimento','_senha']
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

    def busca_pess(buscar_cpf:str,cursor):
    
        pessoa = list(cursor.execute("SELECT * FROM pessoas WHERE cpf = ?",(buscar_cpf)))
        if (len(pessoa)!=0):
            return pessoa[0][0]
        return False

    def cadast_pess(nome:str,endereco:str,cpf:str,data_nascimento:str,senha:str,cursor):

        if Pessoa.busca_pess(cpf,cursor)== False:
            cursor.execute("INSERT INTO pessoas(nome,cpf,data_nascimento,senha) VALUES(?,?,?,?)",(nome,cpf,data_nascimento,senha))
            return True
        return False