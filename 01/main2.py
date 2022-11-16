from pessoaJuridica import PessoaJuridica 

pessoajuridica = PessoaJuridica(
    input('Informe seu nome:> '), 
    input('Informe seu CNPJ:> '), 
    float(input('Informe seu saldo inicial:> ')))

print("="*30, "Menu", "="*30)

print(pessoajuridica)

print("="*30, "Menu", "="*30)

pessoajuridica.segundo_titular = input("Digite o segundo titular: ")

print(pessoajuridica)