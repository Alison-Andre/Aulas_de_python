# declaração
texto = "texto teste"

# quebra de linha 1
quebra = """"texto teste
    pular linha"""

# quebra de linha 2
quebrar = "texto com /n" \
    "quebra de linha"

# Concaternar
nome = "Alison"
sobrenome = "Andre"

nome_completo = nome + sobrenome

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)

print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))

print(f"Nome completo (9a forma): {nome} {sobrenome}")
