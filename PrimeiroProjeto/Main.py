from classePessoaFisica import PessoaFisica

pessoa = PessoaFisica('Michael','086.615.526-05',28)

print(pessoa.getNome())
print(pessoa.getCpf())
print(pessoa.getIdade())


pessoa2 = PessoaFisica('Virginia','000.000.000-01',18)
print(pessoa.getNome())
print(pessoa.getCpf())
print(pessoa.getIdade())