print("---------------------")
print("CALCULADORA SIMPLES")
print("---------------------")

num1 = float(input("Insira o primeiro valor: "))
op = input("Insira o operador: ")
num2 = float(input("Insira o segundo valor: "))

if op == "+" :

    res = num1 + num2
    print (f"O resultado da operação é: {res}")

elif op == "-" :

    res = num1 - num2
    print (f"O resultado da operação é: {res}")

elif op == "*" :

    res = num1 * num2
    print (f"O resultado da operação é: {res}")

elif op == "/" :

    res = num1/num2
    print (f"O resultado da operação é: {res}")

else:

    print("Por favor, insira um operador válido")