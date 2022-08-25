from models.cliente import Cliente
from models.conta import Conta

felicity = Cliente('Felicity Jone', 'felicity@gmain.com', '123.456.789-00', '02/09/1987')
angelina = Cliente('Angelina Jolie', 'angelina@hotmail.com', '987.654.321-01', '08/10/1992')

# print(felicity)

contaf = Conta(felicity)
contaa = Conta(angelina)

print(contaf)
print(contaa)