nome = "Alison"
sobrenome = "Andre"

nome_completo = nome + sobrenome

# Mudar a caixa
# caixa alta
nome_completo.upper()

# caixa baixa
nome_completo.lower()

# capitalizar
nome_completo.capitalize()

# Acessar um caracter da string
nome_completo[0]

# Buscar ocorrências de um caracter
texto = "banana"
ocorrencias = texto.count("a")
print(ocorrencias)  # Saída: 3

# Buscar índice da primeira ocorrência
texto = "Python é uma linguagem de programação"
indice = texto.find("linguagem")
print(indice)  # Saída: 12

# Codificar strings em bytes.
nome.encode()
# Decodificar bytes em string
nome.decode()

# Substituir uma string por outra
texto = "Olá, mundo! O mundo é grande."
novo_texto = texto.replace("mundo", "universo")
print(novo_texto)  # Saída: Olá, universo! O universo é grande.

# Adicionar um separador
frutas = ["maçã", "banana", "laranja"]
string_frutas = ", ".join(frutas) # inicia com o separador que queremos
print(string_frutas)  # Saída: maçã, banana, laranja

# Separa uma string em uma lista
texto = "Olá, mundo! Como vai?"
palavras = texto.split()
print(palavras)  # Saída: ['Olá,', 'mundo!', 'Como', 'vai?']

# Remove os caracteres iniciais e finais
texto = "   Olá, mundo!   "
texto_limpo = texto.strip()
print(texto_limpo)  # Saída: Olá, mundo!

# Verifica se inicia com um caracter específico
nome_completo.startswith("al") # Saída é 'true'

# Verifica se existe ou não um termo dentro da string
"al" in nome_completo # Saída 'true'
"al" not in nome_completo
