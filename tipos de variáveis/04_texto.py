# Declaração
texto = "texto teste"

# Quebra de linha simples
texto = "Linha 1\nLinha 2\nLinha 3"

# Quebra de linha em strings multilinha:
texto_multi_linha = """
Esta é uma string
que ocupa várias linhas.
Cada linha é separada por \n.
"""

# Quebra de linha com concatenação
parte1 = "Parte do texto "
parte2 = "na próxima linha."
texto_completo = parte1 + "\n" + parte2
print(texto_completo)

# Concaternar
nome = "Alison"
sobrenome = "Andre"

nome_completo = nome + sobrenome

print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)

print("Nome completo (3a forma): %s" % nome_completo)
print("Nome completo (4a forma): %s %s" % (nome, sobrenome))

print(f"Nome completo (5 forma): {nome} {sobrenome}")
print("Nome completo (6a forma): {} {}".format(nome, sobrenome))
