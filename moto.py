import sqlite3

class Moto ():
    __slots__ = ['_num_chas','_nome','_marca','_tipo','_ano','_valor','_modelo','_cpfVendedor']
    def __init__(self,num_chas,marca,tipo,ano,valor,modelo,cpfVendedor):
        self._num_chas = num_chas
       
        self._marca = marca
        self._modelo = modelo
        self._tipo = tipo
        self._ano = ano
        self._valor = valor
        self._cpfVendedor=cpfVendedor
    
     
    @property
    def cpfVendedor(self):
        return self._cpfVendedor

    @cpfVendedor.setter
    def cpfVendedor(self,nm):
        self._cpfVendedor = nm
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
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self,val):
        self._modelo = val
    @property
    def num_chas(self):
        return self._num_chas

    def imprimeMoto(self):
        return 'Nome: {} \nMarca: {} \nTipo: {} \nAno: {} \nModelo: {} \n'.format(self._nome,self.marca,self._tipo,self._ano,self._valor,self._modelo)
class CadastroMoto():
    __slots__=['_lista']
    def __init__(self):
        bd = sqlite3.connect('bdMoto.sqlite')
        cursor = bd.cursor()
        motos = """CREATE TABLE IF NOT EXISTS motos(id integer PRIMARY KEY,numero_chassi text NOT NULL,modelo text NOT NULL,
                    marca text NOT NULL,categoria text NOT NULL,ano text NOT NULL,valor float NOT NULL, CPFVendedor text NOT NULL);"""
        cursor.execute(motos)
        bd.commit()
        bd.close()
    def cadastra_moto(self,moto):
        if (self.buscar(moto.num_chas)== None):
            bd = sqlite3.connect('bdMoto.sqlite')
            cursor = bd.cursor()
            cursor.execute('''INSERT INTO motos(numero_chassi,modelo,marca,categoria,ano,valor,CPFVendedor) VALUES (?,?,?,?,?,?,?)''',
            (moto.num_chas,moto.modelo,moto.marca,moto.tipo,moto.ano,moto.valor,moto.cpfVendedor))
            bd.commit()
            bd.close()
            return True
        else:
            return False
    def buscar(self,num_chas):
        bd = sqlite3.connect('bdMoto.sqlite')
        cursor = bd.cursor()
        motos = list(cursor.execute('SELECT * FROM motos WHERE numero_chassi = ?',((num_chas,))))
        if(len(motos)!=0):
            bd.commit()
            bd.close()    
            return motos
        else:
            bd.commit()
            bd.close()
            return None

    def venda(num_chas:str):
        bd = sqlite3.connect('bdMoto.sqlite')
        cursor = bd.cursor()
        cursor.execute('DELETE * FROM motos WHERE numero_chassi = "{}"',(num_chas))
        bd.commit()
        bd.close()