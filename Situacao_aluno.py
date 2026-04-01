#Este programa lê 3 notas de um aluno, calcula sua média e retorna a sua situação.

aluno = input("Digite o nome do aluno: ")
soma = 0

for i in range (1,4):

    nota = float(input(f"Digite a nota {i} do aluno {aluno}: "))

    soma = soma + nota

media = soma/3

if media >= 7:

    print(f"O aluno {aluno} obteve média {media} e está APROVADO!")

elif media >= 5:

    print(f"O aluno {aluno} obteve média {media} e está de RECUPERAÇÃO!")

else:

    print(f"O aluno {aluno} obteve média {media} e está REPROVADO!")
