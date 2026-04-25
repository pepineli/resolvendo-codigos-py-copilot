# Vamos calcular a média de três notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media:.2f}")

if media >= 7:
    print("Aluno APROVADO!")
elif media >= 5:
    print("Aluno em RECUPERAÇÃO!")
else:
    print("Aluno REPROVADO!")