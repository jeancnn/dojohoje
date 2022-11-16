from pessoafisica import Pessoafisica
from pessoaJuridica import PessoaJuridica

pessoafisica = Pessoafisica(input('Informe se nome:> '), input('Informe seu CPF:> '), float(input('Informe seu saldo inicial:> ')))

print('*'*30, 'Menu inicial pessoa física', '*'*30)

print(pessoafisica)

print('*'*30, 'Menu inicial segundo títular', '*'*30)

pessoafisica.segundo_titular = 'Lirinha Boladão'
print(pessoafisica)
