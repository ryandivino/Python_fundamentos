print("---------------")
print("TABUADA SIMPLES")
print("---------------")

n = int(input("Digite um número: "))
print("---------------")

op = input("Digite um operador: ")
print("---------------")


for i in range (1,n+1):

    for k in range(1,11):

        if op == "+":
            resultado = i+k
            print(f"{i} + {k} = {resultado}")
            
        elif op == "-":
        
            resultado = i-k
            print(f"{i} - {k} = {resultado}")

        elif op == "*":

            resultado = i*k
            print(f"{i} X {k} = {resultado}")
        
        elif op == "/":

            resultado = i/k
            print(f"{i} / {k} = {resultado}")
        
        else:

            print("Por favor, insira um operador válido!")

    print("---------------")

