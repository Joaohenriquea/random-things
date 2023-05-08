# Pede ao usuário para inserir a operação desejada
operacao = input("Insira a operação desejada (+, -, *, /): ")

# Pede ao usuário para inserir os números para a operação
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

# Realiza a operação selecionada
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida.")

# Exibe o resultado
print("O resultado é:", resultado)
