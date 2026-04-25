# Vamos verificar se uma palavra é um palíndromo

palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas
palavra_limpa = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_limpa[::-1]

if palavra_limpa == palavra_invertida:
    print(f'"{palavra}" é um PALÍNDROMO!')
else:
    print(f'"{palavra}" NÃO é um palíndromo.')