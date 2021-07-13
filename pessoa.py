import sqlite3
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
class PessoaCadas():
    __slots__=['_lista']
    def __init__(self):
        bd = sqlite3.connect('bdPessoa.sqlite')
        cursor = bd.cursor()
        pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integer PRIMARY KEY,nome text NOT NULL,endereco text NOT NULL,
                    cpf text NOT NULL,data_nascimento text NOT NULL,senha text NOT NULL);"""
        print("OI")
        cursor.execute(pessoas)
        bd.commit()
        bd.close()
    def busca_pess(self,buscar_cpf):
        bd = sqlite3.connect('bdPessoa.sqlite')
        cursor = bd.cursor()
        pessoa = list(cursor.execute("SELECT * from pessoas WHERE cpf = ?",((buscar_cpf,))))
        print(type(pessoa))
        if (len(pessoa)!=0):
            bd.commit()
            bd.close()
            return pessoa
        return None
    def Up_pess(self,p):
        bd = sqlite3.connect('bdPessoa.sqlite')
        cursor = bd.cursor()
        
        if (self.busca_pess(p.cpf)!= None):
            #cursor.execute('INSERT INTO pessoas(nome,endereco,cpf,data_nascimento,senha) VALUES(?,?,?,?,?)',(p.nome,p.endereco,p.cpf,p.data_nascimento,p.senha))
            cursor.execute('UPDATE pessoas SET nome = "%s", endereco = "%s", cpf="%s", data_nascimento="%s" WHERE cpf = "%s"' % (str(p.nome),str(p.endereco),p.cpf,p.data_nascimento))
            bd.commit()
            bd.close()
            return True
        bd.commit()
        bd.close()
        return False

    def cadast_pess(self,p):
        bd = sqlite3.connect('bdPessoa.sqlite')
        cursor = bd.cursor()
        print(type(p.cpf))
        
        if (self.busca_pess(p.cpf)== None):
            cursor.execute('INSERT INTO pessoas(nome,endereco,cpf,data_nascimento,senha) VALUES(?,?,?,?,?)',(p.nome,p.endereco,p.cpf,p.data_nascimento,p.senha))
            bd.commit()
            bd.close()
            return True
        bd.commit()
        bd.close()
        return False