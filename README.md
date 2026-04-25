#  Meus Estudos com Python + GitHub Copilot

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


> Este repositório documenta minha jornada de aprendizado em Python através de 6 desafios práticos. Utilizei o **GitHub Codespaces** como ambiente de desenvolvimento e o **GitHub Copilot** (com auxílio do ChatGPT) como meu copiloto de código.

---

##  Sobre o Projeto

Este projeto faz parte do meu portfólio de estudos na **DIO (Digital Innovation One)**. O objetivo foi praticar conceitos fundamentais de Python resolvendo problemas simples, mas essenciais para quem está começando.

**Ferramentas utilizadas:**
-  Python 3
-  GitHub Codespaces
-  GitHub Copilot / ChatGPT
-  Git & GitHub

---

##  Métodos e Aprendizados por Desafio

### 1️⃣ Concatenação de Dados

**Como fiz:**  
Criei um script que recebe duas entradas do usuário e as une em uma única string.

**Métodos utilizados:**
- `input()` para capturar dados
- Operador `+` para concatenar strings
- Separação com espaço entre as informações

```python
info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")
info_concatenada = info1 + " " + info2
print("As informações concatenadas são:", info_concatenada)
```

---

### 2️⃣ Repetição de Textos

**Como fiz:**  
Recebi uma string e um número inteiro. Usei a multiplicação de strings para repetir o texto.

**Métodos utilizados:**
- `int()` para converter string em número
- Operador `*` para multiplicar strings

```python
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
print(string * numero)
```

---

### 3️⃣ Operações Matemáticas

**Como fiz:**  
Recebi dois números e uma operação (+, -, *, /) e utilizei condicionais para executar a conta correta.

**Métodos utilizados:**
- `float()` para aceitar números decimais
- Estrutura `if/elif/else` para escolher a operação
- Validação de divisão por zero

```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operação inválida!")
```

---

### 4️⃣ Par ou Ímpar

**Como fiz:**  
Recebi um número inteiro e usei o operador de módulo (`%`) para verificar o resto da divisão por 2.

**Métodos utilizados:**
- Operador módulo `%`
- Estrutura condicional `if/else`

```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR!")
```

---

### 5️⃣ Média de Notas

**Como fiz:**  
Recebi três notas, somei todos os valores e dividi por 3. Adicionei uma validação para mostrar se o aluno foi aprovado ou não.

**Métodos utilizados:**
- Conversão com `float()` para notas decimais
- Cálculo aritmético `(n1 + n2 + n3) / 3`
- Formatação com `f-string` e `:.2f` para 2 casas decimais

```python
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
```

---

### 6️⃣ Palíndromo

**Como fiz:**  
Recebi uma palavra ou frase, removi espaços, converti para minúsculas e comparei com a versão invertida.

**Métodos utilizados:**
- `.replace(" ", "")` para remover espaços
- `.lower()` para padronizar maiúsculas/minúsculas
- `[::-1]` para inverter a string (fatiamento com passo negativo)

```python
palavra = input("Digite uma palavra: ")

palavra_limpa = palavra.replace(" ", "").lower()
palavra_invertida = palavra_limpa[::-1]

if palavra_limpa == palavra_invertida:
    print(f'"{palavra}" é um PALÍNDROMO!')
else:
    print(f'"{palavra}" NÃO é um palíndromo.')
```

---

##  Estrutura do Projeto

```
resolvendo-codigos-py-copilot/
├── resolucoes_code/
│   ├── concat_dados.py    # Desafio 1 - Concatenação
│   ├── repet_txt.py       # Desafio 2 - Repetição
│   ├── ope_mat.py         # Desafio 3 - Operações matemáticas
│   ├── par_impar.py       # Desafio 4 - Par ou ímpar
│   ├── media_notas.py     # Desafio 5 - Média de notas
│   └── palindromo.py      # Desafio 6 - Palíndromo
└── README.md
```

---

##  O que eu aprendi com este projeto

- Manipular strings com concatenação, repetição e inversão
- Trabalhar com números inteiros e decimais
- Usar condicionais (`if`, `elif`, `else`) para controle de fluxo
- Aplicar o operador módulo (`%`) para verificar paridade
- Calcular média e classificar resultados
- Inverter strings usando fatiamento (`[::-1]`)
- Versionar código com Git no GitHub Codespaces

---


## 📝 Licença

Este projeto é de uso livre para estudos. Fique à vontade para clonar, modificar e compartilhar!

---

**⭐ Se gostou deste conteúdo, deixe uma estrela no repositório!**
