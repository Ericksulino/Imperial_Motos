from loja import Loja
from pessoa import Vendedor,Cliente
from moto import Moto

lj = Loja()

vend = Vendedor('Erick','Picos','123','16/12/2000')

clie = Cliente('Jose','Geminiano','321','10/01/1970')

mot = Moto('4321','Fan 160','Honda','street','2011',11000.00)

print(lj.cadas_vend(vend))

print(lj.cadas_clie(clie))

print(lj.cadas_moto(mot))

print(lj.busca_vend('123'))

vend.imprimir_vendedor()

print(lj.impri_todas_motos())

print(lj.venda('4321','321','123'))

print(lj.impri_todas_motos())

vend.imprimir_vendedor()